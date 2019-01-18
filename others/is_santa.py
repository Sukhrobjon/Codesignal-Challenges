import re

def isSanta(s):
    not_santa = "Hey, someone! Merry Christmas and have a nice day!"
    santa = "It is Santa! Merry Christmas and a Happy New Year!"
    s = re.sub("[^a-zA-Z'\\-]", " ", s)
    s_lower = s.lower()
    words = s_lower.split()
    # print(words)
    if 'hohoho' in words:
        return santa
    return not_santa
s = "What about HoHoHo?!"

print(isSanta(s))
