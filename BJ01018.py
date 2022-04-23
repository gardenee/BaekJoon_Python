N, M = map(int, input().split())
init = []
for _ in range(N):
    init.append(list(input()))
ans = N * M
for i in range(N-7):
    temp = init[i:i+8]
    for j in range(M-7):
        ans1 = 0
        ans2 = 0
        for k in range(8):
            for l in range(8):
                if k % 2 == 0:
                    if l % 2 == 0 and temp[k][j+l] == 'W':
                        ans1 += 1
                    elif l % 2 == 1 and temp[k][j+l] == 'B':
                        ans1 += 1
                    elif l % 2 == 0 and temp[k][j + l] == 'B':
                        ans2 += 1
                    elif l % 2 == 1 and temp[k][j + l] == 'W':
                        ans2 += 1

                else:
                    if l % 2 == 0 and temp[k][j+l] == 'B':
                        ans1 += 1
                    elif l % 2 == 1 and temp[k][j+l] == 'W':
                        ans1 += 1
                    elif l % 2 == 0 and temp[k][j + l] == 'W':
                        ans2 += 1
                    elif l % 2 == 1 and temp[k][j + l] == 'B':
                        ans2 += 1
        m = min(ans1, ans2)
        if m < ans:
            ans = m

print(ans)
