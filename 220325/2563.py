lst = [[0]*100 for _ in range(100)]

for _ in range(int(input())):
    m, n = map(int, input().split())
    for i in range(m, m+10):
        for j in range(n, n+10):
            lst[i][j] = 1

ans = 0
for i in lst:
    ans += i.count(1)

print(ans)
