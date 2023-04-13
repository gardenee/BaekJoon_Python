from sys import stdin
import heapq

n, m, r = map(int, input().split())
items = list(map(int, input().split()))

INF = 10001
distance = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, stdin.readline().split())
    distance[a][b] = min(distance[a][b], l)
    distance[b][a] = distance[a][b]

for i in range(1, n+1):
    distance[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

answer = 0

for i in range(1, n+1):
    temp = 0
    for j in range(1, n+1):
        if distance[i][j] <= m:
            temp += items[j-1]

    answer = max(answer, temp)

print(answer)
