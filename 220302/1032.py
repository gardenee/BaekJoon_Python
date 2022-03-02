ans = ''
lst = []

for i in range(int(input())):
    lst.append(input())

if len(lst) == 1:
    ans = lst[0]
else:
    for m in range(len(lst[0])):
        for n in range(len(lst)-1):
            if lst[n][m] != lst[n+1][m]:
                ans += '?'
                break
            elif n == len(lst)-2:
                ans += lst[n][m]

print(ans)
