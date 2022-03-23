dic = {}
for i in range(int(input())):
    me = []
    temp = set()
    for _ in range(5):
        me.append(list(input()))
    for a in range(5):
        for b in range(7):
            if me[a][b] == 'X':
                temp.add(str(a)+str(b))
    dic[i+1] = temp

ans = 36
A = 0; B = 0
values = list(dic.values())
for i in range(len(values)-1):
    j = 1
    while i + j < len(values):
        if len(values[i].symmetric_difference(values[i+j])) < ans:
            ans = len(values[i].symmetric_difference(values[i+j]))
            A = i + 1
            B = i + j + 1
        j += 1

print(A, B)
