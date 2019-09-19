def sortByHeight(a):
    indices = sorted([i for i in a if i > 0])
    for index, item in enumerate(a):
        if item == -1:
            indices.insert(index, item)
    print("a " + str(a))
    return indices

a = [-1, 200, 190, 170, -1, -1, 160, 180]

print(sortByHeight(a))
