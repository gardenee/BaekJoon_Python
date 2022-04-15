from sys import stdin

nums = []

for _ in range(int(input())):
    n = int(stdin.readline())
    if n == 0:
        nums.pop()
    else:
        nums.append(n)

print(sum(nums))
