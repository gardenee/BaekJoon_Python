from sys import stdin
from collections import deque

dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    world = [list(map(int, stdin.readline().split())) for _ in range(h)]
    answer = 0

    for i in range(h):
        for j in range(w):
            if world[i][j] == 1:
                answer += 1
                world[i][j] = 0
                queue = deque([[i, j]])

                while queue:
                    x, y = queue.popleft()

                    for n in range(8):
                        nx, ny = x + dx[n], y + dy[n]
                        if 0 <= nx < h and 0 <= ny < w and world[nx][ny] == 1:
                            world[nx][ny] = 0
                            queue.append([nx, ny])

    print(answer)
