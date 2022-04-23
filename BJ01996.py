N = int(input())
mine = []
for i in range(N):
    info = list(input())
    for j in range(N):
        if info[j] != '.':
            mine.append([i+1, j+1, int(info[j])])

map = []
for i in range(N+2):
    map.append([])
    for _ in range(N+2):
        map[i].append(0)

for i in mine:
    map[i[0]][i[1]] = '*'
    if map[i[0]-1][i[1]-1] != '*':
        map[i[0]-1][i[1]-1] += i[2]
    if map[i[0]-1][i[1]] != '*':
        map[i[0]-1][i[1]] += i[2]
    if map[i[0]-1][i[1]+1] != '*':
        map[i[0]-1][i[1]+1] += i[2]
    if map[i[0]][i[1]-1] != '*':
        map[i[0]][i[1]-1] += i[2]
    if map[i[0]][i[1]+1] != '*':
        map[i[0]][i[1]+1] += i[2]
    if map[i[0]+1][i[1]-1] != '*':
        map[i[0]+1][i[1]-1] += i[2]
    if map[i[0]+1][i[1]] != '*':
        map[i[0]+1][i[1]] += i[2]
    if map[i[0]+1][i[1]+1] != '*':
        map[i[0]+1][i[1]+1] += i[2]

for i in range(1, N+1):
    ans = ''
    for j in range(1, N+1):
        if map[i][j] != '*' and map[i][j] >= 10:
            ans += 'M'
        else:
            ans += str(map[i][j])
    print(ans)
