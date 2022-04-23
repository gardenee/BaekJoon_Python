while True:
    N = str(input())
    if N == '0':
        break
    while int(N) >= 10:
        temp = 0
        for i in N:
            temp += int(i)
        N = str(temp)
    print(N)
