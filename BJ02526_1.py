N, P = map(int, input().split())
temp = [N]
while True:
    n = temp[-1] * N % P
    if n in temp:
        print(len(temp) - temp.index(n))
        break
    else:
        temp.append(n)
