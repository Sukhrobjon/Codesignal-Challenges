def digit_rootFunc(n):
    return (n - 1) % 9 + 1

print(digit_rootFunc(20))

def digit_root_sort(arr):
    # arr = sorted(arr)
    digit_root = []
    for i in arr:
        digit_root.append(digit_rootFunc(i))
    root_dict = dict(zip(arr, digit_root))
    
    
    return root_dict


arr = [20, 13, 4, 7]
print(digit_root_sort(arr))


"""const sum = n = > [...n.toString()].reduce((a, b)=> +a + +b),
      array = [13, 20, 7, 4]

array.sort((a, b)= > sum(a) - sum(b) | | a - b)

console.log(array)"""
