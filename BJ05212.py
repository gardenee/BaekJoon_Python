R, C = map(int, input().split())
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

world_map = [list(input()) for _ in range(R)]
future_map = [world_map[i][:] for i in range(R)]

for x in range(R):
    for y in range(C):
        if world_map[x][y] == ".":
            continue

        count_land = 0
        for n in range(4):
            nx, ny = x + dx[n], y + dy[n]
            if 0 <= nx < R and 0 <= ny < C and world_map[nx][ny] == "X":
                count_land += 1

        if count_land < 2:
            future_map[x][y] = "."


start, end = 0, R-1

while "X" not in future_map[start]:
    start += 1

while "X" not in future_map[end]:
    end -= 1


left, right = C-1, 0

for i in range(start, end+1):
    if "X" not in future_map[i]:
        continue
    left = min(left, future_map[i].index("X"))
    right = max(right, C-1-future_map[i][::-1].index("X"))

for i in range(start, end+1):
    print("".join(future_map[i][left:right+1]))
