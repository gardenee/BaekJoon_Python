A, B = map(str, input().split())
ans = 0
B_sum = 0
for b in range(len(B)):
    B_sum += int(B[b])

for a in range(len(A)):
    ans += int(A[a]) * B_sum

print(ans)
