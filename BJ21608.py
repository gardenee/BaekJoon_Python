import heapq

N = int(input())

location = dict()
favor = dict()
classroom = [[0] * N for _ in range(N)]

dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]


def find_seat(my_pick):
    seats, checked = [], []
    for pick in my_pick:
        if pick not in location.keys():
            continue
        for n in range(4):
            x, y = location[pick]
            nx = x + dx[n]
            ny = y + dy[n]

            for i in range(len(seats)):
                s = seats[i]
                if s[2] == nx and s[3] == ny:
                    seats[i][0] -= 1
                    heapq.heapify(seats)
                    break
                continue

            if 0 <= nx < N and 0 <= ny < N and classroom[nx][ny] == 0:
                cnt = 0
                for j in range(4):
                    newx, newy = nx+dx[j], ny+dy[j]
                    if 0 <= newx < N and 0 <= newy < N and classroom[newx][newy] == 0:
                        cnt += 1
                heapq.heappush(seats, [-1, -cnt, nx, ny])

    if seats:
        rtn = heapq.heappop(seats)
        checked.append([rtn[2], rtn[3]])
        return rtn
    else:
        x, y = check_empty()
        return [0, 0, x, y]


def check_empty():
    max = -1
    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if classroom[i][j] == 0:
                cnt = 0
                for n in range(4):
                    nx = i + dx[n]
                    ny = j + dy[n]
                    if 0 <= nx < N and 0 <= ny < N and classroom[nx][ny] == 0:
                        cnt += 1
                if max < cnt:
                    max = cnt
                    x, y = i, j
                    if cnt == 8: break
    return x, y


for i in range(N**2):
    n, a, b, c, d = map(int, input().split())
    favor[n] = [a, b, c, d]

    if i == 0:
        classroom[1][1] = n
        location[n] = [1, 1]
        continue
    seat = find_seat([a, b, c, d])
    classroom[seat[2]][seat[3]] = n
    location[n] = [seat[2], seat[3]]

answer = 0
for i in range(N):
    for j in range(N):
        curr = classroom[i][j]
        cnt = 0
        friend = favor[curr]
        for n in range(4):
            nx, ny = i+dx[n], j+dy[n]
            if 0 <= nx < N and 0 <= ny < N and classroom[nx][ny] in friend:
                cnt += 1

        if cnt == 1:
            answer += 1
        elif cnt == 2:
            answer += 10
        elif cnt == 3:
            answer += 100
        elif cnt == 4:
            answer += 1000

print(answer)
