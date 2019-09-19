from collections import Counter


def num_same_elements(arr_1, arr_2):
    """Counts the number of same elements in a given lists
    Args:
        arr_1(list): first array
        arr_2(list): second array
    Returns:
        same elements(int): number of same elements
    """
    result = set(arr_1).intersection(set(arr_2))
    return len(result)


a = [2]
b = [2, 3, 5]

print(num_same_elements(a, b))