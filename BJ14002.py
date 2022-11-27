import bisect

N = int(input())
nums = list(map(int, input().split()))

index = []
curr = []
for num in nums:
    if not curr or curr[-1] < num:
        index.append(len(curr))
        curr.append(num)
    else:
        idx = bisect.bisect_left(curr, num)
        curr[idx] = num
        index.append(idx)

n = len(curr)
print(n)

answer = []
for i in range(N-1, -1, -1):
    if index[i] == n-1:
        answer.append(nums[i])
        n -= 1

print(*answer[::-1])
