N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B2 = B.copy()
B2.sort(reverse=True)

ans = 0
for i in range(N):
    ans += A[i] * B[B.index(B2[i])]

print(ans)
