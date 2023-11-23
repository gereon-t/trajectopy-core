"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
from typing import Optional
import numpy as np
import xml.etree.ElementTree as ET
from trajectopy_core.trajectory import Trajectory


def color_from_value(value: float, min_value: float, max_value: float) -> str:
    """
    Returns a color string in the format "ff0000ff" (RGBA) for a given value in a range.
    The color is chosen from green (min_value) to red (max_value).
    """
    if value < min_value or value > max_value:
        raise ValueError(f"Value {value} is not in range [{min_value}, {max_value}].")

    # value = (value - min_value) / (max_value - min_value)
    value = (value - min_value) / (max_value - min_value)
    value = 1 - value

    if value < 0.5:
        r = 0
        g = int(255 * value * 2)
    else:
        r = int(255 * (value - 0.5) * 2)
        g = 255

    return f"ff{r:02x}{g:02x}00"


def create_kml(trajectory: Trajectory, color_values: Optional[np.ndarray] = None) -> str:
    if color_values is None:
        color_values = np.zeros(len(trajectory))
    else:
        color_values /= np.max(color_values)

    if len(color_values) != len(trajectory):
        raise ValueError(
            f"Number of colors ({len(color_values)}) must be equal to number of positions ({len(trajectory.pos.xyz)})."
        )

    if trajectory.pos.local_transformer is None:
        raise ValueError(
            "Trajectory must be defined in a well-known coordinate system (EPSG code) to be exported to KML. "
        )
    trajectory.pos.to_epsg(4326)

    kml_file = ET.Element("kml", xmlns="http://earth.google.com/kml/2.1")
    document = ET.SubElement(kml_file, "Document")

    placemark = ET.SubElement(document, "Placemark")
    name = ET.SubElement(placemark, "name")
    name.text = trajectory.name

    style = ET.SubElement(placemark, "Style")
    line_style = ET.SubElement(style, "LineStyle")
    color = ET.SubElement(line_style, "color")
    color.text = "ff0000ff"
    width = ET.SubElement(line_style, "width")
    width.text = "2"

    line_string = ET.SubElement(placemark, "LineString")
    coordinates = ET.SubElement(line_string, "coordinates")

    coordinates.text = "\n".join(f"  {pos[1]:.9f},{pos[0]:.9f},0.000" for pos in trajectory.pos.xyz)

    folder = ET.SubElement(document, "Folder")
    name = ET.SubElement(folder, "name")
    name.text = trajectory.name

    for value, pos in zip(color_values, trajectory.pos.xyz):
        placemark = ET.SubElement(folder, "Placemark")
        name = ET.SubElement(placemark, "name")

        style = ET.SubElement(placemark, "Style")
        icon_style = ET.SubElement(style, "IconStyle")
        icon_color = ET.SubElement(icon_style, "color")
        icon_color.text = color_from_value(value=value, min_value=0, max_value=1)
        scale = ET.SubElement(icon_style, "scale")
        scale.text = "0.2"
        icon_style_icon = ET.SubElement(icon_style, "Icon")
        icon_style_icon_href = ET.SubElement(icon_style_icon, "href")
        icon_style_icon_href.text = "http://maps.google.com/mapfiles/kml/pal2/icon18.png"

        point = ET.SubElement(placemark, "Point")
        coordinates = ET.SubElement(point, "coordinates")
        coordinates.text = f"{pos[1]:.9f},{pos[0]:.9f},0.000"

    tree = ET.ElementTree(kml_file)
    ET.indent(tree, space="", level=0)
    tree.write("test.kml", encoding="utf-8", xml_declaration=True)
