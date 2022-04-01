N = int(input())
Xs = list(map(int, input().split()))
Xs2 = Xs.copy()
Xs2.sort()
ans = {}
cnt = 0
for x in range(len(Xs2)):
    if x == 0:
        ans[Xs2[x]] = 0
    else:
        if Xs2[x] != Xs2[x-1]:
            cnt += 1
            ans[Xs2[x]] = cnt

for i in Xs:
    print(ans[i], end=' ')
