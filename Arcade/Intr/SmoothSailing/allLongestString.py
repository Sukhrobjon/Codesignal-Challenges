def allLongestStrings(inputArray):
    newList = []
    if len(inputArray) == 1 or len(inputArray) == 0:
      newList = inputArray
    else:
        longest = 0
        count = 0
        while count < len(inputArray):
            if len(inputArray[count]) > longest:
                longest = len(inputArray[count])
            count += 1

        index = 0
        while index < len(inputArray):
            if len(inputArray[index]) >= longest:
                longest = len(inputArray[index])
                newList.append(inputArray[index])
            index += 1
    return newList


inputArray =    ["a",
                "abc",
                "cbd",
                "zzzzzz",
                "a",
                "abcdef",
                "asasa",
                "aaaaaa"]

print(allLongestStrings(inputArray))

