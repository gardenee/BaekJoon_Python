N, X = map(int, input().split())
visit = list(map(int, input().split()))

hit, cnt = 0, 1
for i in range(X):
    hit += visit[i]

i, curr = 0, hit
while i+X < len(visit):
    curr = curr - visit[i] + visit[i+X]
    i += 1
    if curr > hit:
        hit, cnt = curr, 1
    elif curr == hit:
        cnt += 1

if hit == 0: print('SAD')
else: print(str(hit)+'\n'+str(cnt))
