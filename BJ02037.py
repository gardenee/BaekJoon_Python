p, w = map(int, input().split())
line = input()

dic = {}
dic2 = {}
alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '122233344455566677778889999'
t = '112312312312312312341231234'
for i in range(27):
    dic[alphabet[i]] = int(num[i])
for i in range(27):
    dic2[alphabet[i]] = int(t[i])

ans = 0
for l in range(len(line)-1):
    ans += int(dic2[line[l]]) * p
    if line[l] != ' ' and dic[line[l]] == dic[line[l+1]]:
        ans += w
ans += int(dic2[line[-1]]) * p

print(ans)
