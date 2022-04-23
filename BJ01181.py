from sys import stdin
N = int(input())
dic = {}
for _ in range(N):
    word = stdin.readline().replace('\n', '')
    dic.setdefault(len(word), [])
    dic[len(word)].append(word)

num = list(dic.keys())
num.sort()
for n in num:
    dic[n] = list(set(dic[n]))
    dic[n].sort()

for i in range(len(num)):
    for j in range(len(dic[num[i]])):
        print(dic[num[i]][j])
