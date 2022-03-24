nums = []
temp = []
N = int(input())
T = 0

for i in range(2 * N - 1):
    if i % 2 == 0:
        n = int(input())
        if T == 1:
            nums.append(temp.pop() * n)
            T = 0
        elif T == 2:
            nums.append(temp.pop() // n)
            T = 0
        else:
            nums.append(n)

    else:
        n = input()
        if n == '*':
            T = 1
            temp.append(nums.pop())
        elif n == '/':
            T = 2
            temp.append(nums.pop())
        elif n == '-':
            nums.append('!')

while True:
    if '!' in nums:
        a = nums.index('!')
        nums[a+1] *= -1
        nums.pop(a)
    else:
        break

print(sum(nums))
