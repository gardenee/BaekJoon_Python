N = int(input())
board = [list(input()) for _ in range(N)]

heart = []
for i in range(N):
    for j in range(N):
        if board[i][j] == '*':
            print(i+2, j+1)
            heart = [i+1, j]
            break
    if heart:
        break

body = []
x = heart[1]-1
tmp = 0
while x >= 0:
    if board[heart[0]][x] == '*':
        tmp += 1
        x -= 1
    else:
        break
body.append(str(tmp))

x = heart[1]+1
tmp = 0
while x < N:
    if board[heart[0]][x] == '*':
        tmp += 1
        x += 1
    else:
        break
body.append(str(tmp))

y = heart[0]+1
tmp = 0
while y < N:
    if board[y][heart[1]] == '*':
        tmp += 1
        y += 1
    else:
        break
body.append(str(tmp))

a, b = y, heart[1]-1
tmp = 0
while a < N:
    if board[a][b] == '*':
        tmp += 1
        a += 1
    else:
        break
body.append(str(tmp))

a, b = y, heart[1]+1
tmp = 0
while a < N:
    if board[a][b] == '*':
        tmp += 1
        a += 1
    else:
        break
body.append(str(tmp))

print(" ".join(body))
