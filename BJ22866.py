N = int(input())
buildings = list(map(int, input().split()))
INF = 100001

answer = [[INF, 0] for _ in range(N)]
stack = []

for i in range(N):
    L = buildings[i]
    while stack:
        if stack[-1][1] <= L:
            stack.pop()
        else:
            break
    if stack:
        answer[i][0] = stack[-1][0]+1
        answer[i][1] = len(stack)
    if not stack or stack[-1][1] > L:
        stack.append([i, L])

stack = []
for i in range(N-1, -1, -1):
    L = buildings[i]
    while stack:
        if stack[-1][1] <= L:
            stack.pop()
        else:
            break
    if stack:
        if abs(answer[i][0]-1-i) > abs(stack[-1][0]-i):
            answer[i][0] = stack[-1][0]+1
        answer[i][1] += len(stack)
    if not stack or stack[-1][1] > L:
        stack.append([i, L])

for i in range(N):
    if answer[i][0] == INF:
        print(0)
    else:
        print(answer[i][1], answer[i][0])
