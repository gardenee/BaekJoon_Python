board = []
for _ in range(9):
    board.append(list(map(int, input().split())))

blank = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append([i, j])


def possible(num, x, y):
    for i in range(9):
        if board[x][i] == num or board[i][y] == num:
            return False

    bx, by = x//3, y//3
    for i in range(3):
        for j in range(3):
            nx = bx*3 + i
            ny = by*3 + j
            if board[nx][ny] == num:
                return False
    return True


def search(n):
    if n == len(blank):
        for i in range(9):
            for j in range(9):
                print(board[i][j], end=" ")
            print()
        exit(0)

    x, y = blank[n][0], blank[n][1]
    for k in range(1, 10):
        if possible(k, x, y):
            board[x][y] = k
            search(n+1)
            board[x][y] = 0

    return


search(0)
