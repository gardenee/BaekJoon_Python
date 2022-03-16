N = int(input())
lst = list(map(int, input().split()))
ans = 0

for i in lst:
    if i == lst.count(i):
        if i > ans:
            ans = i
            i = '!'

if lst == [0]:
    print(-1)
elif (0 in lst) and (ans == 0):
    print(-1)
else:
    print(ans)
