N = int(input())
dic = {}
cls = []
for i in range(N):
    dic.setdefault(i+1, set())
    cls.append(list(map(int, input().split())))

for i in range(N-1):
    for j in range(i+1, N):
        for k in range(5):
            if cls[i][k] == cls[j][k]:
                dic[i+1].add(j+1)
                dic[j+1].add(i+1)

lst = list(map(list, dic.values()))
M = []
for i in range(N):
    if len(M) < len(lst[i]):
        M = lst[i]

for k, v in dic.items():
    if v == set(M):
        print(k)
        break
