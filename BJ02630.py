N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0


def check(x, y, N):
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if paper[i][j] != color:
                return False
    return True


def split(x, y, N):
    global white
    global blue
    if check(x, y, N):
        if paper[x][y] == 0:
            white += 1
        elif paper[x][y] == 1:
            blue += 1
        return
    split(x, y, N//2)
    split(x+N//2, y, N//2)
    split(x, y+N//2, N//2)
    split(x+N//2, y+N//2, N//2)


split(0, 0, N)
print(white)
print(blue)
