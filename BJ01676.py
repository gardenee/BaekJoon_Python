N = int(input())
cnt = 0

for i in range(2, N+1):
    if i % 5 == 0: cnt += 1
    if i % 25 == 0: cnt += 1
    if i % 125 == 0: cnt += 1

print(cnt)
