from sys import stdin

p, m = map(int, input().split())
rooms = []
user_info = dict()

for _ in range(p):
    lv, name = stdin.readline().rstrip().split()
    lv = int(lv)

    new_room = True
    for i in range(len(rooms)):
        room = rooms[i]
        if room[0] < m and abs(room[1]-lv) <= 10:
            rooms[i][0] += 1
            user_info[i].append([name, lv])
            new_room = False
            break

    if new_room:
        user_info[len(rooms)] = [[name, lv]]
        rooms.append([1, lv])

for i in range(len(rooms)):
    if rooms[i][0] != m:
        print("Waiting!")
    else:
        print("Started!")

    players = user_info[i]
    players.sort()
    for p in players:
        print(p[1], p[0])
