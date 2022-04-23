for _ in range(int(input())):
    H, W, N = map(int, input().split())
    if N%H == 0:
        print(str(H)+'{:02}'.format(N//H))
    else:
        print(str(N%H)+'{:02}'.format((N//H)+1))
