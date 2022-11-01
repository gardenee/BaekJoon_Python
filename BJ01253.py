N = int(input())
ipt = list(map(int, input().split()))

cnt = dict()
nums = set()

for n in ipt:
    nums.add(n)
    cnt[n] = cnt.get(n, 0)+1

answer = 0
checked = set()
lst = list(nums)
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if lst[i] * lst[j] == 0: continue
        check = lst[i]+lst[j]
        if check not in checked and check in nums:
            checked.add(check)
            answer += cnt[check]

for key in cnt.keys():
    if key not in checked:
        if key == 0:
            if cnt[key] >= 3: answer += cnt[key]
        else:
            if 0 in nums and cnt[key] > 1: answer += cnt[key]

print(answer)
