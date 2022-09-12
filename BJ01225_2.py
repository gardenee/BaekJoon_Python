A, B = map(str, input().split())
ans = 0

for a in range(len(A)):
    for b in range(len(B)):
        ans += int(A[a]) * int(B[b])

print(ans)
