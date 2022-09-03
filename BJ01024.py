N, L = map(int, input().split())
nope = True

for i in range(2, 101):
    N -= (i-1)

    if N < 0:
        break
    if i < L:
        continue
    if N % i == 0:
        nope = False
        for n in range(i):
            print(N//i + n, end=" ")
        break

if nope:
    print(-1)
