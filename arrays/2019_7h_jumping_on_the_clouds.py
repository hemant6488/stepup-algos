def jumpingOnClouds(numberOfClouds, clouds):
    currentPos, jumps = 0, 0
    # 0 0 0 1 0 0
    while currentPos < numberOfClouds - 1:
        if (currentPos < numberOfClouds - 2) and clouds[currentPos + 2] == 0:
            currentPos += 2
            jumps += 1
        elif clouds[currentPos + 1] == 0:
            currentPos += 1
            jumps += 1
        else:
            jumps += 1

    return jumps


if __name__ == '__main__':
    numberOfClouds = int(input())
    clouds = [int(z) for z in input().strip().split()]
    print(jumpingOnClouds(numberOfClouds, clouds))

