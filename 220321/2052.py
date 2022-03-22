N = 1 / 2 ** int(input())
if 'e' in str(N):
    N = str('%0.300f' % N)
    n = 0
    for i in range(len(N)-1, 1, -1):
        if N[i] != '0':
            n = i
            break
    print(N[:n+1])
else:
    print(N)