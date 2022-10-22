N = int(input())
line = list(map(int, input().split()))

answer = [0] * N

for i in range(N):
    curr = line[i]
    j, cnt = 0, 0
    while cnt < curr:
        if answer[j] == 0:
            cnt += 1
        j += 1
    while answer[j]:
        j += 1
    answer[j] = i+1

for i in range(N):
    print(answer[i], end=" ")
