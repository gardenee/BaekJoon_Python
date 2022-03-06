연두이름 = input()
N = int(input())
dic = dict()
이름들 = []

for _ in range(N):
    이름들.append(input())
이름들.sort()

for n in range(N):
    이름 = 이름들[n]
    L = 0
    O = 0
    V= 0
    E = 0
    L = 이름.count('L') + 연두이름.count('L')
    O = 이름.count('O') + 연두이름.count('O')
    V = 이름.count('V') + 연두이름.count('V')
    E = 이름.count('E') + 연두이름.count('E')
    dic[이름] = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100

점수 = list(dic.values())
M = max(점수)

for k, v in dic.items():
    if v == M:
        print(k)
        break