from collections import Counter
def commonCharacterCount(s1, s2):
    occurance = (Counter(s1) & Counter(s2))
    # print(occurance.values())
    number  = sum(occurance.values())
    return number

s1 = "zzzz"
s2 = "zzzzzz"

print(commonCharacterCount(s1, s2))
