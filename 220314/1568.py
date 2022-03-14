N = int(input())
i = 1
ans = 0
while N > 0:
    if N - i >= 0:
        ans += 1
        N -= i
        i += 1
    else:
        i = 1

print(ans)