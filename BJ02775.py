for _ in range(int(input())):
    k = int(input())
    n = int(input())
    arr = [0] * 15
    for i in range(15):
        arr[i] = [0] * 15
    for i in range(15):
        arr[0][i] = i
        arr[i][1] = 1
    for i in range(2, n+1):
        for j in range(1, k+1):
            arr[j][i] = arr[j-1][i] + arr[j][i-1]
    print(arr[k][n])
