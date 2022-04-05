from math import comb

for _ in range(int(input())):
    N, M = map(int, input().split())
    if N == M:
        print(1)
    else:
        r = M-N
        ans = 0
        i = 0
        while i <= (r-1) and i <= N:
            ans += comb(N+1, i+1) * comb(r-1, i)
            i += 1
        print(ans)
