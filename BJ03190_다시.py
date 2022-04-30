from sys import stdin
from collections import deque

dir = 0
N = int(input())
board = [([0] * N) for _ in range(N)]
for i in range(int(input())):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1
board[0][0] = "S"
flag = 1

def turn(dir, cmd):
    if cmd == "D":
        return (dir + 1) % 4
    elif cmd == "L":
        return (dir - 1) % 4

x = 0; y = 0
count = 0
temp = deque()
temp.append([0, 0]);

for _ in range(int(input())):
    n, cmd = stdin.readline().rstrip().split()
    T = count
    for _ in range(int(n) - T):
        count += 1
        if dir == 0:
            x += 1
        elif dir == 1:
            y += 1
        elif dir == 2:
            x -= 1
        elif dir == 3:
            y -= 1
        if x >= N or y >= N or x < 0 or y < 0:
            flag = 0
            break
        temp.append([x, y])
        if board[y][x] == 0:
            board[y][x] = "S"
            t = temp.popleft()
            board[t[1]][t[0]] = 0
        elif board[y][x] == 1:
            board[y][x] = "S"
        elif board[y][x] == "S":
            flag = 0
            break
    dir = turn(dir, cmd)
    if flag == 0:
        break

if flag == 1:
    while True:
        count += 1
        if dir == 0:
            x += 1
        elif dir == 1:
            y += 1
        elif dir == 2:
            x -= 1
        elif dir == 3:
            y -= 1
        if x >= N or y >= N or x < 0 or y < 0:
            flag = 0
            break
        temp.append([x, y])
        if board[y][x] == 0:
            board[y][x] = "S"
            t = temp.popleft()
            board[t[1]][t[0]] = 0
        elif board[y][x] == 1:
            board[y][x] = "S"
        elif board[y][x] == "S":
            flag = 0
            break
        if flag == 0:
            break

print(count)
