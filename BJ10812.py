N, M = map(int, input().split())
basket = [i for i in range(N+1)]

for _ in range(M):
    start, end, mid = map(int, input().split())
    copy = basket[:]
    a, b = end-mid+1, mid-start

    for i in range(a):
        basket[start+i] = copy[mid+i]
    for i in range(b):
        basket[start+a+i] = copy[start+i]

print(*basket[1:])
