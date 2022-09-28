from sys import stdin

N = int(input())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
zero, plus, minus = 0, 0, 0


def check(i, j, N):
    num = arr[i][j]
    for x in range(i, i+N):
        for y in range(j, j+N):
            if num != arr[x][y]:
                return False
    return True


def split(i, j, N):
    global zero, plus, minus

    if check(i, j, N):
        num = arr[i][j]
        if num == 0:
            zero += 1
        elif num == 1:
            plus += 1
        else:
            minus += 1
        return

    n = N//3
    dx = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    dy = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    for k in range(9):
        split(i+n*dx[k], j+n*dy[k], n)


split(0, 0, N)
print(minus)
print(zero)
print(plus)
