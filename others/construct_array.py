def construct_array(size):
    x = [t + 1 for t in range(size)]
    if size %  2 != 0:
        x1 = x[:size//2 + 1]
        x2 = x[size//2 + 1:]
        x2.reverse()
        x2.append("")
    else:
        x1 = x[:size//2]
        x2 = x[size//2:]
        x2.reverse()
    new_x = []
    for i in range(len(x1)):
        new_x.append(x1[i])
        new_x.append(x2[i])

    return(new_x if len(new_x) == size else new_x[:-1])
    

size = 7

print(construct_array(size))






