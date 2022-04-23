lst = []
for i in range(int(input())):
    temp = list(map(int, input().split()))
    temp.append(1)
    lst.append(temp)
    for j in range(i):
        if lst[j][0] > temp[0] and lst[j][1] > temp[1]:
            temp[2] += 1
        elif lst[j][0] < temp[0] and lst[j][1] < temp[1]:
            lst[j][2] += 1

ans = []
for i in range(len(lst)):
    ans.append(str(lst[i][2]))

print(' '.join(ans))
