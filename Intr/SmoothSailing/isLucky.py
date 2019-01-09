def isLucky(n):
    arr = [int(i) for i in str(n)]
    half = len(arr) // 2
    return sum(arr[:half]) == sum(arr[half:len(arr)])

print(isLucky(02210))


