N, m, M, T, R = map(int, input().split())
time = 0
n = 0
now = m

if m + T > M:
    print(-1)
else:
    while N != n:
        if now + T <= M:
            now += T
            n += 1
            time += 1
        else:
            if now - R > m:
                now -= R
            else:
                now = m
            time += 1
    print(time)