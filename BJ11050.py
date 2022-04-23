N, K = map(int, input().split())
son = 1
mom = 1

n = N
while n > (N-K):
    son *= n
    n -= 1

n = 2
while n <= K:
    mom *= n
    n += 1

print(son//mom)
