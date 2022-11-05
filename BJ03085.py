N = int(input())
candy = [list(input()) for _ in range(N)]


def max_candy():
    cnt_x, cnt_y, temp_x, temp_y = 0, 0, 0, 0
    for x in range(N):
        for y in range(N):
            if y < N-1 and candy[x][y] == candy[x][y+1]:
                temp_y += 1
            else:
                cnt_y = max(cnt_y, temp_y+1)
                temp_y = 0

            if y < N-1 and candy[y][x] == candy[y+1][x]:
                temp_x += 1
            else:
                cnt_x = max(cnt_x, temp_x+1)
                temp_x = 0

    return max(cnt_x, cnt_y)


answer = max_candy()

for i in range(N):
    for j in range(N):
        if i < N-1 and candy[i][j] != candy[i+1][j]:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            answer = max(answer, max_candy())
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
        if j < N-1 and candy[i][j] != candy[i][j+1]:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            answer = max(answer, max_candy())
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]

print(answer)
