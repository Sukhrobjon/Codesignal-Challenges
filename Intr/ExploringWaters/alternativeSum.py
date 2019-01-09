def alternatingSums(a):
    oddTeam = 0
    evenTeam = 0
    for i in range(len(a)):
        if i % 2 == 0:
            oddTeam += a[i]
        else:
            evenTeam += a[i]
    return [oddTeam, evenTeam]
    

def alternatingSums2(a):
    return [sum(a[::2]), sum(a[1::2])]

a = [50, 60, 60, 45, 70]
print(alternatingSums(a))

print(alternatingSums2(a))
