WD = "Pass with distinction"
A = "Number not accepted"


def average(number: int) -> str:
    """Returns string according to the value"""
    if not isinstance(number, int):
        raise ValueError("Integer required")
    if number < 0 or number > 100:
        raise ValueError(A)
    elif number >= 0 and number < 45:
        return "Fail"
    elif number <= 80:
        return "Pass"
    elif number <= 100:
        return WD
