"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import logging
from enum import Enum, auto
from typing import List, Tuple

import matplotlib.tri as mtri
import networkx as nx
import numpy as np
from scipy.signal import find_peaks
from scipy.spatial import KDTree

from trajectopy_core.util.datahandling import lengths_from_xyz, moving

# logger configuration
logger = logging.getLogger("root")


class Sorting(Enum):
    CHRONO = auto()
    SPATIAL = auto()

    def __str__(self) -> str:
        return "spatial" if self == Sorting.SPATIAL else "chrono"


SORTING_DICT = {"spatial": Sorting.SPATIAL, "chrono": Sorting.CHRONO}


class SpatialSorter:
    """Class representing a spatial sorter.

    This class sorts position spatially by computing the
    moving-least-squares approximation and the minimum-spanning-tree
    of the point set.

    Spatially in the context of a trajectory means, that after sorting,
    the trajectory is a function of its arc length and not a function
    of time. Spatially sorting a trajectory only makes sense if the
    trajectory was repeated multiple times.

    A sorter object should sort input data and provide at least the
    following interface:
    - idx_sort: Index to establish the sorting starting from unordered raw data
    - function_of: Parameterization of the sorted data
    """

    def __init__(
        self,
        xyz: np.ndarray,
        discard_missing: bool = True,
    ) -> None:
        """Initialization of the SpatialSorter

        Args:
            xyz (np.ndarray): Input points for sorting
            mls_dist (float, optional): Neighborhood distance for
                                        moving-least-squares
                                        approximation in meters.
                                        It describes the radius of a
                                        kd-tree ball-query.
                                        Defaults to 0.05.
            mls_it_th (float, optional): Threshold when to stop
                                         performing the iterative
                                         moving-least-squares
                                         approximation in meters.
                                         It describes the average point
                                         movement after an mls iteration.
                                         Defaults to 0.01.
            discard_missing (bool, optional): If set to True, points
                                              dicarded during delaunay
                                              triangulation are also
                                              discarded during sorting.
                                              Alternatively, missing
                                              points can be inserted
                                              'manually' after the
                                              actual sorting.
                                              Defaults to True.
        """
        self._mls_unsorted = xyz
        self.discard_missing = discard_missing
        self._idx_sort: list = []

        self.reconstruct()

    def __len__(self) -> int:
        """Returns number of elements the class can sort

        Returns:
            length, interger
        """
        return len(self.idx_sort)

    @property
    def idx_sort(self) -> List[int]:
        """How can unsorted arrays be sorted?"""
        return self._idx_sort

    @property
    def function_of(self) -> np.ndarray:
        """How should the points be parameterized AFTER sorting?"""
        return lengths_from_xyz(np.array(self.sort(self.mls_unsorted)))

    @property
    def direction(self) -> int:
        """Detect lap directions"""
        return _detect_direction(self._mls_unsorted)

    @property
    def mls_unsorted(self) -> np.ndarray:
        """Returns (unsorted) mls positions used for sorting"""
        return self._mls_unsorted

    @property
    def lap_indices(self) -> np.ndarray:
        """Returns the indices of each lap

        The lap indices are indicating at which index
        a new lap begins
        """
        return detect_laps_by_length(np.array(self.sort(self.mls_arc_lengths, inverse=True)))

    @property
    def num_laps(self) -> int:
        """Returns the number of laps"""
        return max(len(self.lap_indices) - 2, 1)

    @property
    def mls_arc_lengths(self) -> np.ndarray:
        """Returns trajectory lengths from mls positions"""
        return lengths_from_xyz(self.mls_unsorted)

    def reconstruct(self) -> list:
        """Reconstructs the spatial sorting of the given points

        Spatially sorts the positions by constructing the
        minimum-spanning-tree of the positions.
        Finally, by performing up to 3 breadth-first-searched
        within the mst, the spatial sorting can be reconstructed

        This method also takes care of inserting missing points
        or assuring that the direction of travel is kept during
        sorting.

        Returns:
            list: Sort index
        """
        # sort
        self._idx_sort, idx_missing = reconstruct_spatial_sorting(xyz=self._mls_unsorted)

        if len(idx_missing) > 0 and not self.discard_missing:
            # insert missing points
            # some unsorted points need to be inserted into the sort vector
            logger.info("Inserting missing points %i", len(idx_missing))
            missing_points: list = self._mls_unsorted[idx_missing, :].tolist()

            mls_sorted = self.mls_unsorted[self._idx_sort, :]
            for m_i, p in zip(idx_missing, missing_points):
                self._idx_sort, mls_sorted = _insert_point(m_i, p, self._idx_sort, mls_sorted)

        # Set start position of lap as the position with the maximum z-value
        self._idx_sort = begin_with(idx=self._idx_sort, begin=int(np.argmax(self._mls_unsorted[:, 2])))

        # check if direction is correct
        mls_sorted = self.sort(array=self._mls_unsorted)
        if _detect_direction(np.array(mls_sorted)) != self.direction:
            logger.info("Adjusted direction of travel!")
            self._idx_sort = np.flipud(self.idx_sort).tolist()

        return self._idx_sort

    def sort(self, array: np.ndarray, inverse: bool = False) -> np.ndarray:
        """Function that applies the sorting index to an array / list

        Args:
            array (np.ndarray]): array that needs to get sorted
            inverse (bool, optional): Specifies whether the sorting
                                      should be inverted. If set to
                                      'True', already sorted data can
                                      be 'unsorted'.
                                      Defaults to False.

        Returns:
            np.ndarray: Sorted array
        """
        idx_sort = np.array(np.argsort(self.idx_sort) if inverse else self.idx_sort, dtype=int)

        return array[idx_sort, :] if array.ndim > 1 else array[idx_sort]


def _insert_point(
    missing_point_index: int,
    missing_point: np.ndarray,
    idx_sort: list,
    xyz_sorted: np.ndarray,
) -> Tuple[list, np.ndarray]:
    """Inserts a point into an existing sorting

    This method should only be called internally by the
    reconstruct method of the SpatialSorter class

    Args:
        missing_point_index (int): index of the missing point
                                   i.e. its position in the
                                   unsorted array of points
        missing_point (np.ndarray): coordinates of the missing
                                    point that should be inserted
        idx_sort (list): list of indices that establish the spatial
                         sorting in which the missing point needs
                         to be inserted.
        xyz_sorted (np.ndarray): coordinates of the sorted points
                                 (sorted using idx_sort)

    Returns:
        Tuple[list, np.ndarray]: idx_sort and xyz_sorted with inserted
                                 point
    """
    # xyz_list
    xyz_list: list = xyz_sorted.tolist()

    # create KDTree for point set
    tree = KDTree(xyz_sorted)

    # get nearest neighbor
    _, ii = tree.query(missing_point, k=2)

    # min idx
    min_idx = min(ii)
    # max idx
    max_idx = max(ii)

    idx_diff = abs(max_idx - min_idx)

    # find these neighbours in the sort index list to know where the neighbors
    # occur in the sorting. We should place the point in between both
    if idx_diff == 1:
        idx_sort.insert(min_idx + 1, missing_point_index)
        xyz_list.insert(min_idx + 1, missing_point)
    else:
        diff = int(idx_diff / 2)
        idx_sort.insert(min_idx + diff, missing_point_index)
        xyz_list.insert(min_idx + diff, missing_point)

    return idx_sort, np.array(xyz_list)


def reconstruct_spatial_sorting(xyz: np.ndarray) -> Tuple[list, list]:
    """Reconstruct the spatial sorting

    Given a set of points inside a numpy array,
    this method reconstruct the spatial sorting of
    those points using a minimum-spanning-tree.
    The minimum-spanning-tree is a cycle-free graph
    that connects all points while minimizing its
    edge lengths.

    Args:
        xyz (np.ndarray): Input points that should be sorted

    Returns:
        Tuple[list, list]: Index that establishes a spatial sorting
                           as well as a list containing the indices
                           of missing points. This can be the case
                           if the delaunay triangulation necessary
                           for the minimum-spanning-tree computation
                           discards some points if they are almost
                           identical. If no points are missing, the
                           list will be empty.
    """
    # create minimum spanning tree
    mst, missing = compute_mst(xyz)

    # mst = nx.minimum_spanning_tree(delaunay, weight='weight', algorithm='prim')
    logger.info("searching for endpoints")

    # find possible candidates for endpoints
    d1_nodes = [n for n in range(len(mst.nodes)) if mst.degree[n] == 1]
    logger.info("found %i nodes of degree 1", len(d1_nodes))

    if len(d1_nodes) == 2:
        end_nodes = d1_nodes
    else:
        # breadth-first search starting from a arbitrary d1-node
        bfs_a = _breadth_first_search(mst, d1_nodes[0])

        # the last visited node is one endpoint
        e_1 = _breadth_first_search(mst, bfs_a[-1])[-1]
        # perform breadth first search again, starting from this node
        e_2 = _breadth_first_search(mst, e_1)[-1]

        # final end nodes
        end_nodes = [e_1, e_2]

    shortest_path_lengths = nx.shortest_path_length(mst, end_nodes[0], end_nodes[1], weight="weight")
    logger.info("found minimum path length: %.3f m", shortest_path_lengths)

    # breadth-first-search through mst to reconstruct the order
    logger.info("reconstructing point order")
    idx_sort = _breadth_first_search(mst, root=end_nodes[0])

    return idx_sort, missing


def begin_with(idx: list, begin: int) -> list:
    """Reorganizes list so that 'begin' is the first
    value in the list

    Args:
        idx (list): index that should be reorganized
        begin (int): value of the new first element

    Returns:
        list: reorganized list whose first value is now
              'begin'
    """
    idx_start = idx.index(begin)
    idx_max_sort = idx[idx_start:]
    idx_max_sort.extend(idx[:idx_start])
    return idx_max_sort


def compute_mst(xyz: np.ndarray) -> Tuple[nx.Graph, list]:
    """Function that computes a Minimum-Spanning-Tree
    using the matplotlib implementation. This implementation
    may skip some (nearly) colinear points.

    Args:
        xyz (np.ndarray): 2d / 3d positions used for mst computation

    Returns:
        Tuple[nx.Graph, list]: networkx.Graph object of the mst and
                               list of missing point indices if any
                               points are missing due to colinearity
    """
    num_points = len(xyz)
    logger.info("building delaunay triangulation")
    triang = mtri.Triangulation(x=xyz[:, 0], y=xyz[:, 1])
    edges = triang.edges

    # vertex indices of triangulation compared to initial point set
    set1 = set(list(range(num_points)))
    set2 = set(np.unique(np.r_[edges[:, 0], edges[:, 1]]).tolist())

    # missing vertices where dropped due to colinearity
    missing = list(sorted(set1 - set2))

    # costs
    e_diffs = xyz[edges[:, 1], :] - xyz[edges[:, 0], :]
    e_costs = np.linalg.norm(e_diffs, axis=1)

    logger.info("computing minimum spanning tree...")

    # add edges to nx graph
    delaunayt = nx.Graph()
    delaunayt.add_nodes_from(range(num_points))
    delaunayt.add_weighted_edges_from(np.c_[edges, e_costs])
    mst = nx.minimum_spanning_tree(delaunayt)
    logging.info("%i points were discarded during delaunay triangulation!", len(missing))

    return mst, missing


def _breadth_first_search(graph: nx.Graph, root: int) -> list:
    """Performs a breadth first search

    Args:
        graph (nx.Graph): networkx.Graph object
        root (int): index of starting node for breadth-first-search

    Returns:
        list: list of visited nodes
    """
    edges = nx.bfs_edges(graph, root)
    return [root] + [int(v) for _, v in edges]


def _detect_direction(xyz: np.ndarray) -> int:
    """Detects the direction of travel using polar coordinates

    This only works if the points describe a somewhat circular
    trajectory which circulates around the origin of the
    coordinate frame.

    Args:
        xyz (np.ndarray): input positions

    Returns:
        int: -1 / 1 indicating direction of travel
    """
    th = np.arctan2(xyz[:, 1], xyz[:, 0])
    pSign = len(np.where(np.diff(th) > 0)[0])
    nSign = len(np.where(np.diff(th) < 0)[0])

    return np.sign(pSign - nSign)


def detect_laps_by_length(lengths: np.ndarray) -> np.ndarray:
    """
    Detect laps by detecting jumps in unsorted trajectory lengths
    """
    # median filter
    x = moving(x=lengths, win_size=10, function=np.median)

    # differences
    d = np.abs(np.diff(x))

    # find peaks (larger than 90% of the length of a single lap)
    locs = find_peaks(d, height=0.9 * max(lengths))[0]
    return np.r_[0, locs, len(lengths)]


def complete_lap_dist(xyz, dist_th: float = 0.5) -> np.bool_:
    """
    Function to determine if lap is complete
    A lap is considered as complete, if the distance between
    the starting point and the end point is below a specified
    distance
    """

    first = xyz[0, :]
    last = xyz[-1, :]

    diff = first - last
    dist = np.linalg.norm(diff)

    return dist < dist_th


def infer_sort_index(sorting: Sorting, tstamps: np.ndarray):
    """Infers the sort index from the sorting and timestamps"""
    return np.argsort(np.argsort(tstamps)) if sorting == Sorting.SPATIAL else np.argsort(tstamps)
