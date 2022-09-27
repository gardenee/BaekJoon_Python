def dfs(i, result, op):
    global _max
    global _min
    if i == N:
        _min = min(_min, result)
        _max = max(_max, result)
        return
    for j in range(4):
        if op[j] != 0:
            if j == 0:
                temp = result + nums[i]
            elif j == 1:
                temp = result - nums[i]
            elif j == 2:
                temp = result * nums[i]
            elif j == 3 and result >= 0:
                temp = result // nums[i]
            else:
                temp = - (-result // nums[i])
            op[j] -= 1
            dfs(i+1, temp, op)
            op[j] += 1


N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))

_max = -1000000000
_min = 1000000000

dfs(1, nums[0], op)
print(_max)
print(_min)
