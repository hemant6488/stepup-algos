def hourglassSum(arr):
    sums = []
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            hourglassSum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            sums.append(hourglassSum)

    return max(sums)

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append([int(z) for z in input().strip().split()])

    # print(arr)
    print(hourglassSum(arr))
