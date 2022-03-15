N, L = map(int, input().split())
n = 0
i = 1

while n < N:
    if str(L) in str(i):
        i += 1
    else:
        n += 1
        i += 1

print(i-1)
