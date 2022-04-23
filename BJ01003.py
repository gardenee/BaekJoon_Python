arr = [0] * 41
arr[0] = [1, 0]
arr[1] = [0, 1]

for _ in range(int(input())):
    N = int(input())
    if arr[N] == 0:
        n = arr.index(0)
        while n <= N:
            arr[n] = [arr[n-2][0] + arr[n-1][0], arr[n-2][1] + arr[n-1][1]]
            n += 1

    print(str(arr[N][0]), str(arr[N][1]))
