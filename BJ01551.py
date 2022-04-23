N, K = map(int, input().split())
A = list(map(int, input().replace(',', ' ').split()))

for _ in range(K):
    temp = []
    for i in range(N-1):
        temp.append(A[i+1]-A[i])
    A = temp
    N -= 1

ans = ''
for i in A:
    if ans != '':
        ans += ','
    ans += str(i)

print(ans)
