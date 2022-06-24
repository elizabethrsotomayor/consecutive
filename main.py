def consecutive(arr: list, a: int, b: int) -> bool:
    """
    Given a list of unique integers arr and two integers a and b, determine whether or not a and b appear
    consecutively in arr and return a boolean value.
    :param arr:
    :param a:
    :param b:
    :return:
    """
    num_str = str(a) + ", " + str(b)
    reverse = str(b) + ", " + str(a)
    return num_str in str(arr) or reverse in str(arr)
