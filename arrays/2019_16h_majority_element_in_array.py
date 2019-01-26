import time


def getMajorityElement(elementCount, elements):
    dictionary = {}
    for element in elements:
        if element in dictionary.keys():
            dictionary[element] += 1
        else:
            dictionary[element] = 1

    keys = list(dictionary.keys())
    values = list(dictionary.values())

    maxCount = max(values)
    if maxCount > elementCount//2:
        return keys[values.index(maxCount)]
    else:
        return -1



if __name__ == "__main__":
    totalCases = int(input())
    for _ in range(totalCases):
        elementCount = int(input())
        elements = [int(z) for z in input().strip().split(" ")]
        
        start = time.time()
        output = getMajorityElement(elementCount, elements)
        print(output)



