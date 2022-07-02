N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum = 0
cnt = dict()

for i in range(N):
    sum += A[i] - B[i]
    cnt.setdefault(sum, 0)
    cnt[sum] += 1

answer = 0
for key in cnt.keys():
    val = cnt[key]
    if key == 0:
        val += 1
    answer += val * (val-1) // 2

print(answer)