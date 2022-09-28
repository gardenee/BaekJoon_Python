from sys import stdin

N = int(input())
answer = 0
stack = [[int(input()), 1]]

for _ in range(N-1):
    curr = int(stdin.readline())

    while stack and stack[-1][0] < curr:
        answer += stack.pop()[1]

    if stack and stack[-1][0] == curr:
        answer += stack[-1][1]
        stack[-1][1] += 1
        if len(stack) > 1: answer += 1
    else:
        if stack: answer += 1
        stack.append([curr, 1])

print(answer)
