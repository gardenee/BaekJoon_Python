from sys import stdin

N = int(input())
answer = 0
stack = [int(input())]

for _ in range(N-1):
    curr = int(stdin.readline())
    n = 0
    cnt = 0

    while stack:
        temp = stack.pop()
        n += 1
        if temp > curr:
            stack.append(temp)
            break
        elif temp == curr:
            cnt += 1

    answer += n
    for _ in range(cnt+1):
        stack.append(curr)

print(answer)
