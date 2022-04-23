K = int(input())
temp = []
for _ in range(K):
    temp.append([])

str = input()

i = 0; j = 0; n = 0
while n < len(str):
    temp[i].append(str[n])
    if j % 2 == 0:
        if i < K-1:
            i += 1
        else:
            j += 1
    else:
        if i > 0:
            i -= 1
        else:
            j += 1
    n += 1

ans = ''
for i in range(K):
    for j in range(len(temp[i])):
        ans += temp[i][j]

print(ans)
