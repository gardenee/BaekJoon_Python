N = int(input())
towers = list(map(int, input().split()))
ref = {}

for i in range(N):
    ref[towers[i]] = i+1

stack = []
answer = []
answer.append('0')
stack.append(towers[0])

for i in range(1, N):
    curr = towers[i]
    while stack:
        temp = stack.pop()
        if temp > curr:
            answer.append(str(ref[temp]))
            stack.append(temp)
            break
    if not stack:
        answer.append('0')
    stack.append(curr)

print(' '.join(answer))
