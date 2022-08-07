from sys import stdin

T = int(input())
for _ in range(T):
    W, N = map(int, stdin.readline().split())
    trash = W
    distance = 0
    for i in range(N):
        x, w = map(int, stdin.readline().split())
        if trash - w < 0:
            distance += 2 * x
            trash = W - w
        elif trash == w:
            distance += 2 * x
            trash = W
        else:
            trash -= w

        if i == N-1 and trash != W:
            distance += 2 * x

    print(distance)
