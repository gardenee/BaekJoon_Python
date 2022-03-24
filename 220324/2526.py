N, P = map(int, input().split())
t = 0
temp = [N]
while True:
    if t == 0:
        n = N
        t = 1
        temp.append(n)
    else:
        n = temp[-1] * N % P
        if n in temp:
            print(len(temp) - temp.index(n))
            break
        else:
            temp.append(n)
