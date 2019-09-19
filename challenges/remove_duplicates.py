from collections import Counter


def remove_all_duplicates(s):
    """Remove all the occurance of the duplicated values
    Args:
        s(str): input string
    Returns:
        unique values(str): all unique values
    """
    unique_s = ""
    s_counter = Counter(s)
    for key, value in s_counter.items():
        if value == 1:
            unique_s += key
    return unique_s


s = "zzzzzzz"

print(remove_all_duplicates(s))
