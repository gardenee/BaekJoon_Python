M, N = map(int, input().split())
tot = M * N - N
ans = 0
i = 0
while tot > 0:
    i += 1
    ans += 1
    tot -= M - i
    if tot > 0:
        ans += 1
        tot -= N - i

print(ans)