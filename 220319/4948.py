from sys import stdin
while True:
    N = int(stdin.readline())
    if N == 0:
        break
    arr = [1] * (2*N + 1)
    arr[0] = 0
    arr[1] = 0
    for i in range(2, 2*N+1):
        if arr[i] == 1:
            for j in range(2*i, 2*N+1, i):
                arr[j] = 0
    arr = arr[N+1:]
    print(arr.count(1))
