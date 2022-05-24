def check(cmpd, idx, lst):
    cmpd += "1"
    temp = ""
    for i in range(len(cmpd)):
        curr = cmpd[i]
        if ord(curr) < 65:
            if temp == "C":
                lst[idx][0] += int(curr)
            elif temp == "H":
                lst[idx][1] += int(curr)
            elif temp == "O":
                lst[idx][2] += int(curr)
            temp = ""
        else:
            if temp == "C":
                lst[idx][0] += 1
            elif temp == "H":
                lst[idx][1] += 1
            elif temp == "O":
                lst[idx][2] += 1
            temp = curr
    return lst


a, b = input().split("+")
b, c = b.split("=")
lst = [a, b, c]
count = [[0]*3, [0]*3, [0]*3]
for i in range(3):
    count = check(lst[i], i, count)

t = 0
for i in range(1, 11):
    for j in range(1, 11):
        for k in range(1, 11):
            if count[0][0] * i + count[1][0] * j == count[2][0] * k and count[0][1] * i + count[1][1] * j == count[2][1] * k and count[0][2] * i + count[1][2] * j == count[2][2] * k:
                print(i, j, k)
                t = 1
                break
        if t == 1:
            break
    if t == 1:
        break
