def GDC(a, b):
    x = max(a, b)
    y = min(a, b)

    while y != 0:
        temp = y
        y = x % y
        x = temp

    return x


N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))

n = nums[0]
for i in range(N-1):
    nums[i] = abs(nums[i+1] - nums[i])
nums[-1] = abs(nums[-1] - n)

curr = nums[0]
for i in range(1, N):
    curr = GDC(curr, nums[i])

answer = set()
for i in range(2, int(curr**0.5)+1):
    if curr % i == 0:
        answer.add(i)
        answer.add(curr//i)
answer.add(curr)
answer = list(answer)
answer.sort()
for n in answer:
    print(n, end=" ")
