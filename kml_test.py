import logging
from trajectopy_core.trajectory import Trajectory
from trajectopy_core.kml import create_kml
import numpy as np

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def main():
    trajectory = Trajectory.from_file("scripts/2023-03-02.traj")
    trajectory.apply_index(np.arange(0, len(trajectory), 10))
    create_kml(trajectory=trajectory, color_values=trajectory.pos.z)
    # with open("2019-11-25.kml", "w", encoding="utf-8") as f:
    #     f.write(kml_file)


if __name__ == "__main__":
    main()
