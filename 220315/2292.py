a = 1
ans = 1
N = int(input())
if N == 1:
    print(1)
else:
    while True:
        ans += 1
        N = N - 6*a
        if N <= 1:
            print(ans)
            break
        else:
            a += 1
