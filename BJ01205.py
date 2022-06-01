from sys import stdin

N, score, P = map(int, stdin.readline().split())
ranking = list(map(int, stdin.readline().split()))

ans = -1
if N == P and ranking[-1] >= score: ans = -1
else:
    if not ranking:
        if P == 0: ans = -1
        else: ans = 1
    elif ranking[-1] > score: ans = N+1
    else:
        for i in range(N):
            if ranking[i] <= score:
                ans = i+1
                break
print(ans)
