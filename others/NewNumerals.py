import string
def newNumerals(number):
    a = list(string.ascii_uppercase)
    b = []
    for index in range(len(a)):
        if number == a[index]:
            outerCounter = index
    innerCounter = 0
    while (innerCounter <= outerCounter):
        str1 = a[innerCounter]
        str2 = a[outerCounter]
        b.append(str1 + " + "+ str2)
        innerCounter +=1
        outerCounter -=1
    return b
number = 'G'
print(newNumerals(number))