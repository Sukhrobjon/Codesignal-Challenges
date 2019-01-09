# number one solution 
def isIPv4AddressBest(s):
    p = s.split('.')
    print(p)
    return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)


# my Solution
def isIPv4Address(inputString):
    inputString = inputString + '.'
    print(inputString)
    start = 0
    ipNum = []
    for i in range(len(inputString)):
        if inputString[i] == '.':
            target = (inputString[start:i])
            if target != '' and target.isdigit():
                target = int(inputString[start:i])
            else:
                target = -1
            ipNum.append(target)
            start = i + 1
    return all(0 <= x <= 255 for x in ipNum) and len(ipNum) == 4


s = "172.16.254.1"

print(isIPv4AddressBest(s))
