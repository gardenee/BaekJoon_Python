import sys
sys.setrecursionlimit(10**5)

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))


def up(board):
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        k = 0
        temp = 0
        for j in range(N):
            if board[j][i] > 0:
                if temp == 0:
                    temp = board[j][i]
                elif temp == board[j][i]:
                    new_board[k][i] = temp * 2
                    temp = 0
                    k += 1
                else:
                    new_board[k][i] = temp
                    temp = board[j][i]
                    k += 1
        if temp != 0:
            new_board[k][i] = temp

    return new_board


def down(board):
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        k = N-1
        temp = 0
        for j in range(N-1, -1, -1):
            if board[j][i] > 0:
                if temp == 0:
                    temp = board[j][i]
                elif temp == board[j][i]:
                    new_board[k][i] = temp * 2
                    temp = 0
                    k -= 1
                else:
                    new_board[k][i] = temp
                    temp = board[j][i]
                    k -= 1
        if temp != 0:
            new_board[k][i] = temp

    return new_board


def left(board):
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        k = 0
        temp = 0
        for j in range(N):
            if board[i][j] > 0:
                if temp == 0:
                    temp = board[i][j]
                elif temp == board[i][j]:
                    new_board[i][k] = temp * 2
                    temp = 0
                    k += 1
                else:
                    new_board[i][k] = temp
                    temp = board[i][j]
                    k += 1
        if temp != 0:
            new_board[i][k] = temp

    return new_board


def right(board):
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        k = N-1
        temp = 0
        for j in range(N-1, -1, -1):
            if board[i][j] > 0:
                if temp == 0:
                    temp = board[i][j]
                elif temp == board[i][j]:
                    new_board[i][k] = temp * 2
                    temp = 0
                    k -= 1
                else:
                    new_board[i][k] = temp
                    temp = board[i][j]
                    k -= 1
        if temp != 0:
            new_board[i][k] = temp

    return new_board


def move(board, n):
    if n == 0:
        return up(board)
    elif n == 1:
        return down(board)
    elif n == 2:
        return right(board)
    elif n == 3:
        return left(board)


def dfs(board, cnt):
    global answer
    if cnt == 0:
        for i in range(N):
            answer = max(answer, max(board[i]))
        return

    for i in range(4):
        dfs(move(board, i), cnt-1)


answer = 0
dfs(board, 5)
print(answer)
