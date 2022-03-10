dic = {}
al = list('abcdefghijklmnopqrstuvwxyz')
for a in al:
    dic.setdefault(a, 0)

while True:
    try:
        line = input().replace(' ', '').replace('\n', '')
        for l in line:
            dic[l] += 1
    except:
        break

M = max(dic.values())
ans = []
for k, v in dic.items():
    if v == M:
        ans.append(k)
ans.sort()
answer = ''
for a in ans:
    answer += a

print(answer)
