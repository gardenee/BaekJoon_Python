N, M = map(int, input().split())
castle = []
caution_M = 0
caution_N = 0

for _ in range(N):
    castle.append(list(input()))

for i in castle:
    if not ('X' in i):
        caution_M += 1


castle_rotate = []
for i in range(M):
    castle_rotate.append([])
    for _ in range(N):
        castle_rotate[i].append(0)

for i in range(N):
    for j in range(M):
        castle_rotate[j][-i] = castle[i][j]

for i in castle_rotate:
    if not ('X' in i):
        caution_N += 1

print(max(caution_M, caution_N))