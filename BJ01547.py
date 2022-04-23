dic = {1: 1, 2: 0, 3: 0}
for _ in range(int(input())):
    a, b = map(int, input().split())
    dic[a], dic[b] = dic[b], dic[a]

for k, v in dic.items():
    if v == 1:
        print(k)
        break

if not (1 in dic.values()):
    print(-1)