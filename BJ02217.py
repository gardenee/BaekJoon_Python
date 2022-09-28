from sys import stdin

N = int(input())
arr = [int(stdin.readline()) for _ in range(N)]
arr.sort(reverse=True)
answer = arr[0]
cnt = 1

for i in range(1, N):
    cnt += 1
    answer = max(answer, arr[i] * cnt)

print(answer)
