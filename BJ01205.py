N, score, P = map(int, input().split())
ranking = list(map(int, input().split()))

if
elif ranking[-1] >= score:
    print(-1)
else:
    for i in range(P):
        if ranking[i] <= score:
            print(i+1)
            break
