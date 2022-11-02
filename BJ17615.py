N = int(input())
balls = list(input())

cnt, red, blue = 0, 0, 0
start, end = 0, 0
for i in range(N):
    if balls[i] == 'B':
        blue += 1
    elif balls[i] == 'R':
        red += 1

    if i != 0:
        if balls[i-1] != balls[i]: cnt += 1

for i in range(N):
    if balls[i] == balls[0]:
        start += 1
    else:
        break

for i in range(N-1, -1, -1):
    if balls[i] == balls[-1]:
        end += 1
    else:
        break

if balls[0] == balls[-1]:
    if balls[0] == 'B':
        blue -= max(start, end)
    else:
        red -= max(start, end)
else:
    if balls[0] == 'B':
        blue -= start
        red -= end
    else:
        blue -= end
        red -= start

print(min(blue, red))
