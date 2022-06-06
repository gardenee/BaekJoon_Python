N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, input())))

ans = 0
for x in range(N):
    for y in range(M):
        d = 1
        while y+d < M and x+d < N:
            if arr[x][y] == arr[x][y+d] == arr[x+d][y] == arr[x+d][y+d]:
                ans = max(ans, (d+1)**2)
            d += 1

if ans == 0: ans = 1
print(ans)
