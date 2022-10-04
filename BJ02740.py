N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

for n in range(N):
    for k in range(K):
        temp = 0
        for m in range(M):
            temp += A[n][m] * B[m][k]
        print(temp, end=" ")
    print()
