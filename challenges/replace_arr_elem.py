def array_replace(input_array, elem_to_replace, substitution_elem):

    for i, elem in enumerate(input_array):
        if elem == elem_to_replace:
            print(elem)
            input_array[i] = substitution_elem
    return input_array


a = [1, 2, 1]

print(array_replace(a, 1, 3))