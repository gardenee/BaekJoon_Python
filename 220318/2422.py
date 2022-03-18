N, M = map(int, input().split())
dic = {}
for i in range(1, N+1):
    temp = []
    for j in range(i+1, N+1):
        temp.append(j)
    dic[i] = temp

for _ in range(M):
    a, b = map(int, input().split())
    dic[min(a, b)].remove(max(a, b))

ans = 0
for i in range(1, N):
    for j in range(len(dic[i])):
        for k in range(len(dic[dic[i][j]])):
            if dic[dic[i][j]][k] in dic[i]:
                ans += 1

print(ans)