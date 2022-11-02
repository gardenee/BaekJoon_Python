N, S = map(int, input().split())
nums = list(map(int, input().split()))

i, j, sum, answer = 0, 0, nums[0], N+1
while j < N:
    if j == N-1:
        while sum >= S and i <= j:
            answer = min(answer, j-i+1)
            sum -= nums[i]
            i += 1
        break
    if sum < S:
        j += 1
        sum += nums[j]
    else:
        answer = min(answer, j-i+1)
        sum -= nums[i]
        i += 1

if answer == N+1:
    answer = 0

print(answer)
