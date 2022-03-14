N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

for _ in range(2):
    x = 0
    ans = 0
    for i in range(N):
        if lst[i] > x:
            x = lst[i]
            ans += 1
    lst = lst[::-1]
    print(ans)
