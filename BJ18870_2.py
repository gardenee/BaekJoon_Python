N = int(input())
Xs = list(map(int, input().split()))
order = list(set(Xs))
order.sort()
ans = []
for i in range(N):
    ans.append(str(order.index(Xs[i])))

print(' '.join(ans))
