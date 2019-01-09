def repeatedString(s, n):
    stringList = list(s)
    occurranceInSingleString = stringList.count('a')
    stringLength = len(stringList)

    fullStringOccurances = n // stringLength
    partialOccurance = n % stringLength
    
    partialCount = stringList[0:partialOccurance].count('a')
    totalCount = (fullStringOccurances * occurranceInSingleString) + partialCount
    
    return totalCount

if __name__ == '__main__':
    string = input().strip()
    totalChars = int(input())

    print(repeatedString(string, totalChars))
