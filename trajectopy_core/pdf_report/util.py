import base64


def number_to_string(number: float) -> str:
    return f"{number:.3f}"


def image_to_base64(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string
