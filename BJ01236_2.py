N, M = map(int, input().split())
castle = []
caution_M = 0
caution_N = 0

for _ in range(N):
    castle.append(list(input()))

for i in castle:
    if not ('X' in i):
        caution_M += 1

for i in range(M):
    temp = []
    for j in range(N):
        temp.append(castle[j][i])
    if not ('X' in temp):
        caution_N += 1

print(max(caution_M, caution_N))