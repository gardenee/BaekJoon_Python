N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
check = [0] * (d+1)
check[c] = 1

def count():
    cnt = 0
    for i in range(d+1):
        if check[i] > 0: cnt += 1
    return cnt


for i in range(k):
    check[sushi[i]] += 1
answer = count()

for i in range(N):
    check[sushi[i%N]] -= 1
    check[sushi[(i+k)%N]] += 1
    answer = max(answer, count())

print(answer)
