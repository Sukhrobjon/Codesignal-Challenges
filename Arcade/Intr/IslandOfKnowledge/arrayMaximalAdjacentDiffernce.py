def arrayMaximalAdjacentDifference(inputArray):
    diff = []
    for i in range(0, len(inputArray) - 1):
        diff.append(abs(inputArray[i+1] - inputArray[i]))
    return max(diff)
    # return max(abs(inputArray[i] - inputArray[i+1])) for i in range(len(inputArray) - 1)


arr = [2, 4, 1, 0]
arr2 = [10, 11, 13]

print(arrayMaximalAdjacentDifference(arr2))
# print("output: " + str(arrayMaximalAdjacentDifference(arr)))
# print("expected output: 3")
# print("output: " + str(arrayMaximalAdjacentDifference(arr2)))
# print("expected output: 2")
