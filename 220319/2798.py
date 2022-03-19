N, M = map(int, input().split())
cards = list(map(int, input().split()))

ans = 0
for i in range(N-2):
    j = 1
    k = 1
    while i + j + k <= N - 1:
        while i + j + k <= N - 1:
            x = cards[i] + cards[i+j] + cards[i+j+k]
            if x <= M:
                if ans < x:
                    ans = x
            k += 1
        k = 1
        j += 1

print(ans)
