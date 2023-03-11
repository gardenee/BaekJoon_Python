N, M = map(int, input().split())
basket = [i for i in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    for n in range((j-i+1)//2):
        basket[i+n], basket[j-n] = basket[j-n], basket[i+n]

print(*basket[1:])
