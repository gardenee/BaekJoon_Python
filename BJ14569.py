lectures = []
for _ in range(int(input())):
    lectures.append(list(map(int, input().split()))[1:])

for _ in range(int(input())):
    time_table = [False] * 51
    available = list(map(int, input().split()))[1:]
    for i in range(len(available)):
        time_table[available[i]] = True

    possible = 0
    for lecture in lectures:
        cnt = 0
        for time in lecture:
            if time_table[time]:
                cnt += 1
            else:
                cnt = 0
                break
        if cnt:
            possible += 1

    print(possible)
