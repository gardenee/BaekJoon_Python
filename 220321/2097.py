N = int(input())
X = 4
m = 1
n = 1
ans = 4
if N <= 2:
    ans = 4

while X < N:
    if m == n:
        m += 1
        X += n + 1
        ans += 2
    else:
        n += 1
        X += n + 1
        ans += 2

print(ans)
