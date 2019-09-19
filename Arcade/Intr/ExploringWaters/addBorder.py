def add_border(a):
    b = []
    newLen = len(a[0]) + 2
    border = ""
    for _ in range(newLen):
        border += "*"
    b.append(border)
    for item in range(0, len(a)):
        b.append("*" + a[item] + "*")
    b.append(border)

    return b


p = ["aaa", "bbb", "ccc"]

print(add_border(p))
