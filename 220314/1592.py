N, M, L = map(int, input().split())

ans = 0
lst = []
for _ in range(N):
    lst.append(0)

i = 0
while True:
    lst[i] += 1
    if lst[i] == M:
        break
    if lst[i] % 2 == 1:
        i = (i + L) % N
    else:
        i = (N + i - L) % N
    ans += 1

print(ans)
