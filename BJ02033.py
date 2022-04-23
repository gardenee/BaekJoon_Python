N = int(input())
i = 1
while 10 ** i < N:
    N = round(N+0.1, -i)
    i += 1
print(int(N))