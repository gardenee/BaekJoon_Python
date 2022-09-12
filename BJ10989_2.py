from sys import stdin
N = int(input())
dic = {}
nums = []
for _ in range(N):
    n = int(stdin.readline())
    dic.setdefault(n, 0)
    dic[n] += 1
    nums.append(n)

nums.sort()

for i in range(1, len(nums)):
    if nums[i] != nums[i-1]:
        dic[nums[i]] += dic[nums[i-1]]

arr = [0] * N

for i in nums:
    n = dic[i] - 1
    while True:
        if arr[n] == 0:
            arr[n] = str(i)
            break
        else:
            n -= 1

print('\n'.join(arr))
