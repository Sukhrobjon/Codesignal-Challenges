def array_replace(input_array, old_item, new_item):
    output_array = [new_item if x == old_item else x for x in input_array]
    return output_array

arr = [1, 2, 1]
old = 1
new_item = 3
print(array_replace(arr, old, new_item))
