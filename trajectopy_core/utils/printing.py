"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""


def dict2table(
    input_dict: dict,
    title: str,
    key_width: int = 16,
    value_width: int = 8,
    key_value_filler: str = " : ",
    decimal_places: int = 3,
) -> str:
    """
    Converts a dictionary to a formatted table string.

    Args:
        input (dict): The dictionary to be converted to a table.
        title (str): The title of the table.
        key_width (int, optional): The width of the key column. Defaults to 16.
        value_width (int, optional): The width of the value column. Defaults to 8.
        key_value_filler (str, optional): The string used to separate the key and value columns. Defaults to " : ".
        decimal_places (int, optional): The number of decimal places to display for float values. Defaults to 3.

    Returns:
        str: The formatted table string.

    Example:
        >>> my_dict = {"key1": 123.456, "key2": "value2"}
        >>> dict2table(my_dict, "My Table")
        '\n ______________________\n| ------ My Table ------ |\n| key1            : 123.456 |  \n| key2            : value2  |  \n|________________________|\n'
    """
    if not key_value_filler:
        key_value_filler = " "

    # <|><space>item<space><|>
    left_right_width = 4

    # how much characters are the field rows
    max_value_width = max(value_width, max(len(str(value)) for value in input_dict.values()))
    max_key_width = max(key_width, max(len(str(key)) for key in input_dict))
    field_lengths = max_key_width + max_value_width + len(key_value_filler) + left_right_width

    # width of the table
    len_title = len(title) + 2 * left_right_width
    table_width = max(len_title, field_lengths)
    modulo_width = table_width % 2

    # how many dashes must be set for title padding
    title_padding = max(0, table_width - (len_title))
    right_title_padding = title_padding % 2 if title_padding != 0 else 0
    title_padding //= 2

    title_blank_padding = " " if modulo_width != 0 else ""
    # how many blank spaces must be set after the field row to match the table width
    table_width += modulo_width
    field_padding = max(0, table_width - field_lengths - 1)

    table_str = ""
    table_str += f"\n {'_'*(table_width-left_right_width)}\n"
    table_str += f"| {'-'*title_padding} {title} {'-'*(title_padding + right_title_padding)}{title_blank_padding} |\n"
    for key, value in input_dict.items():
        if isinstance(value, float):
            number_formatter = f".{decimal_places}f"
        else:
            value = str(value)
            number_formatter = ""
        table_str += f"| {key:<{max_key_width}}{key_value_filler}{value:<{max_value_width}{number_formatter}}{' '*field_padding}|\n"
    table_str += f"|{'_'*(table_width-left_right_width)}|\n"

    return table_str


def list2box(
    input_list: list,
    title: str = "",
    upper_boundary: bool = True,
    lower_boundary: bool = True,
    field_length: int = 0,
) -> str:
    """
    Converts a list to a formatted box string.

    Args:
        input_list (list): The list to be converted to a box.
        title (str, optional): The title of the box. Defaults to "".
        upper_boundary (bool, optional): Whether to include an upper boundary. Defaults to True.
        lower_boundary (bool, optional): Whether to include a lower boundary. Defaults to True.
        field_length (int, optional): The width of each field in the box. Default to 0 (auto).

    Returns:
        str: The formatted box string.

    Example:
        >>> my_list = ["item1", "item2", "item3"]
        >>> list2box(my_list, "My Box")
        '┌─────────── My Box ───────────┐\n│ item1                       │\n│ item2                       │\n│ item3                       │\n└─────────────────────────────┘\n'
    """
    if not input_list:
        return ""

    # <|><space>item<space><|>
    left_right_width = 4

    # how much characters are the field rows
    field_lengths = field_length if field_length > 0 else max(len(str(item)) for item in input_list) + left_right_width

    # width of the table
    len_title = len(title) + 2 * left_right_width
    table_width = max(len_title, field_lengths)
    modulo_width = table_width % 2

    # how many dashes must be set for title padding
    title_padding = max(0, table_width - (len_title))
    right_title_padding = title_padding % 2 if title_padding != 0 else 0
    title_padding //= 2

    title_blank_padding = " " if modulo_width != 0 else ""
    # how many blank spaces must be set after the field row to match the table width
    table_width += modulo_width

    table_str = ""
    if upper_boundary:
        table_str += f"\n {'_'*(table_width-left_right_width)}\n"

    if title:
        table_str += (
            f"| {'-'*title_padding} {title} {'-'*(title_padding + right_title_padding)}{title_blank_padding} |\n"
        )

    for item in input_list:
        table_str += f"| {item:<{field_lengths-left_right_width}}|\n"

    if lower_boundary:
        table_str += f"|{'_'*(table_width-left_right_width)}|\n"

    return table_str
