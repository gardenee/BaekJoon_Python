lst = [[0]*100 for _ in range(100)]

for _ in range(4):
    m, n, x, y = map(int, input().split())
    for i in range(m, x):
        for j in range(n, y):
            lst[i][j] = 1

ans = 0
for i in lst:
    ans += i.count(1)

print(ans)
