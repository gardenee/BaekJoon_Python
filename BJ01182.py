N, M = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0


def dfs(idx, _sum):
    global answer
    if idx != 0 and _sum == M:
        answer += 1

    for i in range(idx, N):
        dfs(i+1, _sum + nums[i])


dfs(0, 0)

print(answer)
