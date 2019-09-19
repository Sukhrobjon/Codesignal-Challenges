def areSimilar(a, b):
    # countA = countB = 0
    # for item in range(len(b)):
    #     if a[item] in b:
    #         countA += 1
    #         print("a item" + str(a[item]))
    # for item in range(len(b)):
    #     if b[item] in a:
    #         countB += 1
    # print(countA)
    # print(countB)
    a.sort()
    b.sort()
    return a == b



a = [1, 2, 3]
b = [2, 1, 3]

print(areSimilar(a, b))
