from sys import stdin
for _ in range(int(input())):
    N = int(stdin.readline())
    arr = [1] * (N+1)
    arr[0] = 1
    arr[1] = 1
    for i in range(2, N+1):
        if arr[i] == 1:
            for j in range(2*i, N+1, i):
                arr[j] = 0

    a = N//2
    while a > 1:
        if arr[a] == 1 and arr[N-a] == 1:
            print(a, N-a)
            break
        else:
            a -= 1
