from sys import stdin

N, M, B = map(int, input().split())
ground = []
for _ in range(N):
    ground.append(list(map(int, stdin.readline().split())))

top = 0
bottom = 256
blocks = 0
for i in range(N):
    for j in range(M):
        curr = ground[i][j]
        blocks += curr
        if curr < bottom:
            bottom = curr
        if curr > top:
            top = curr

top = min((blocks + B) // (N*M), top)
top = min(top, 256)

answer = 2 * (blocks - bottom * N * M)
height = bottom
prev = 256 * 500 * 500 * 2

for h in range(top, bottom-1, -1):
    time = 0
    for i in range(N):
        for j in range(M):
            curr = ground[i][j]
            if curr > h:
                time += (curr - h) * 2
            elif curr < h:
                time += h - curr

    if time < answer:
        answer = time
        height = h
    elif time == answer:
        height = max(h, height)

    if prev < time:
        break
    else:
        prev = time

print(answer, height)
