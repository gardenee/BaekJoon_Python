N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]


def check(i, j, N):
    ref = arr[i][j]
    for x in range(i, i+N):
        for y in range(j, j+N):
            if arr[x][y] != ref:
                return False
    return True


def split(i, j, N):
    if check(i, j, N):
        return str(arr[i][j])

    return '(' + split(i, j, N//2) + split(i, j+N//2, N//2) + split(i+N//2, j, N//2) + split(i+N//2, j+N//2, N//2) + ')'


print(split(0, 0, N))
