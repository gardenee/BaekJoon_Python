N = int(input())
room = []
for _ in range(N):
    room.append(list(input()))

ans1 = 0
for x in range(N):
    temp = []
    for i in range(N):
        if room[x][i] == '.':
            temp.append(i)
    for i in range(len(temp)-1):
        if temp[i] + 1 == temp[i+1]:
            ans1 += 1
            for j in range(i, len(temp)-1):
                if temp[j] + 1 == temp[j+1]:
                    temp[j] = -1
                else:
                    break

ans2 = 0
for x in range(N):
    temp = []

    for i in range(N):
        if room[i][x] == '.':
            temp.append(i)
    for i in range(len(temp)-1):
        if temp[i] + 1 == temp[i+1]:
            ans2 += 1
            for j in range(i, len(temp) - 1):
                if temp[j] + 1 == temp[j+1]:
                    temp[j] = -1
                else:
                    break
                    
print(ans1, ans2)
