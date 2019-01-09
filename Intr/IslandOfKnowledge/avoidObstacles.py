def avoidObstacles(inputArray):

    for i in range(1, max(inputArray)):
        jump = any([x for x in inputArray if not x % i])
        if not jump:
            return i
arr = [3, 5, 6, 7, 9]

print(avoidObstacles(arr))
# def exam(n):
#     jump = 1
#     for i in n:
#         if i % jump != 0:

