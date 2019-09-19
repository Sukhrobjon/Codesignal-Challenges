def find_first_duplicate(arr):
    """
    Return the number for which the second occurrence has a smaller index
    than the second occurrence of the other number does. If there are no 
    such elements, return -1.
    """

    if len(arr) == len(set(arr)):
        return -1

    # for each value in the list:
    # i check if I saw the value before if i see the value before
    # check if value is not equal to len(arr) that means we already grabbed the 2nd
    # occurance of the element I add it to the dictionary with the current
    # index if it is the 1st occurance of the elem set the value equal to none

    ind_set = set()

    for elem in arr:
        if elem in ind_set:
            return elem
        else:
            ind_set.add(elem)
    # # finds the min value and returns the key associated with that value
    # return min(ind_dict, key=ind_dict.get)
"""
a: [2, 1, 3, 5, 3, 2] => 3
a: [2, 2] => 2
a: [5, 5, 5, 5, 5] => 5

"""
a = [2, 1, 3, 5, 3, 2]

print(find_first_duplicate(a))
