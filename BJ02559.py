N, K = map(int, input().split())
T = list(map(int, input().split()))

ans = [0] * (N-K+1)
for i in range(K):
    ans[0] += T[i]

for i in range(1, N-K+1):
    ans[i] = ans[i-1] + T[K+i-1] - T[i-1]

print(max(ans))
