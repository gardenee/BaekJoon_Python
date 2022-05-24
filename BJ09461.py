from sys import stdin

arr = [0] * 101
arr[1] = 1
arr[2] = 1
arr[3] = 1
arr[4] = 2
arr[5] = 2

T = int(input())

for _ in range(T):
    N = int(stdin.readline())

    if arr[N] != 0:
        print(arr[N])

    else:
        n = N
        while arr[n] == 0:
            n -= 1

        while n <= N:
            arr[n] = arr[n-5] + arr[n-4] + arr[n-3]
            n += 1
        print(arr[N])
