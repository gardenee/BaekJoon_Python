N = int(input())
nums = list(map(int, input().split()))

cnt = dict()
for n in nums:
    cnt.setdefault(n, 0)
    cnt[n] += 1

answer = []
stack = []
for i in range(N-1, -1, -1):
    curr = cnt[nums[i]]
    ngf = -1
    while stack:
        temp = stack.pop()
        if cnt[temp] > curr:
            ngf = temp
            stack.append(temp)
            break
    stack.append(nums[i])
    answer.append(ngf)

for i in range(N-1, -1, -1):
    print(answer[i], end=" ")
