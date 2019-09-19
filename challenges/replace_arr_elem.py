def array_replace(input_array, elem_to_replace, substitution_elem):
    """Replace all occurance of the elem_to_replace with substitution elements
    """
    for i, elem in enumerate(input_array):
        if elem == elem_to_replace:
            # substitute the element
            input_array[i] = substitution_elem
    return input_array


a = [1, 2, 1]

print(array_replace(a, 1, 3))
