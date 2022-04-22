N = int(input())
nums = list(map(int, input().split()))

stack = []
answer = []
answer.append(-1)
stack.append(nums.pop())

for _ in range(N-1):
    curr = nums.pop()
    while stack:
        temp = stack.pop()
        if temp > curr:
            stack.append(temp)
            answer.append(temp)
            break
    if not stack:
        answer.append(-1)
    stack.append(curr)

for _ in range(N):
    print(answer.pop(), end=" ")
