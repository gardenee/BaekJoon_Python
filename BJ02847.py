N = int(input())
answer = 0
level = [int(input()) for _ in range(N)]

for i in range(N-1, 0, -1):
    prev = level[i]
    curr = level[i-1]
    if curr >= prev:
        answer += curr - prev + 1
        level[i-1] = prev-1

print(answer)
