import math

M = int(input())
N = int(input())
ans = []

for i in range(M, N+1):
    if int(math.sqrt(i)) == math.sqrt(i):
        ans.append(i)

if ans == []:
    print(-1)
else:
    print(sum(ans))
    print(ans[0])
