# number one solution 
def is_ipv4_address(s):
    """
        Return True if 's' is a valid IPv4 address
    """
    # split the string on dots
    s_split = s.split('.')
    
    return len(s_split) == 4 and all(num.isdigit() and 0 <= int(num) < 256 for num in s_split)


# my Solution
def isIPv4Address(inputString):
# I should have thought about using .split() function
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

print(is_ipv4_address(s))
