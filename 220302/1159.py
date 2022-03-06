lst = []
for _ in range(int(input())):
    lst.append(input())
lst.sort()

dic = dict()
for a in lst:
    if not a[0] in dic:
        dic[a[0]] = 1
    else:
        dic[a[0]] = dic[a[0]] + 1

ans = ''
for key, value in dic.items():
    if value >= 5:
        ans += key

if ans == '':
    print('PREDAJA')
else:
    print(ans)
