"""This function uses round to test some cases"""


def wrapper_round(x):
    """This function uses round to test some cases"""
    if not isinstance(x, (int, float)):
        raise ValueError("Decimal number required")
    if isinstance(x, int):
        x = float(x)
    if x.is_integer():
        return int(x)
    return round(x, 1)
