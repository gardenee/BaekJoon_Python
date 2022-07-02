S = int(input())
n = 1

while S >= n*(n+1)//2:
    if S == n*(n+1)//2:
        n += 1
        break
    n += 1

if S == 1: print(1)
else: print(n-1)
