N, M = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(N)]

for i in range(N):
    ipt = list(input())
    for j in range(M):
        matrix[i][j] = abs(matrix[i][j] - int(ipt[j]))

answer = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1 and i <= N-3 and j <= M-3:
            answer += 1
            for x in range(3):
                for y in range(3):
                    matrix[i+x][j+y] = abs(matrix[i+x][j+y]-1)
    if sum(matrix[i]):
        answer = -1
        break

print(answer)
