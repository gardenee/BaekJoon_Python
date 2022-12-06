from sys import stdin

for _ in range(int(input())):
    M, N, x, y = map(int, stdin.readline().split())

    k = x
    while k <= M * N:
        if k % N == y % N:
            break
        k += M

    if k > M * N:
        k = -1

    print(k)
