N = int(input())

i = 0
while 2 ** i < N:
    i += 1

if N == 2 ** i:
    print(N)
else:
    print((N - 2 ** (i-1)) * 2)
