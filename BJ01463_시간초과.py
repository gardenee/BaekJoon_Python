X = int(input())
curr = [X]
ans = 0

while(True):
    ans += 1
    temp = list()
    for t in curr:
        if t % 3 == 0:
            temp.append(t//3)
        if t % 2 == 0:
            temp.append(t//2)
        temp.append(t-1)
    if 1 in temp: break
    curr = temp

print(ans)
