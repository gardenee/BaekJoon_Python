N = int(input())
stones = list(map(int, input().split()))

curr, answer = 0, 0
min_sum, max_sum = 0, 0

for stone in stones:
    if stone == 1:
        curr += 1
    elif stone == 2:
        curr -= 1

    answer = max(answer, abs(curr - min_sum))
    answer = max(answer, abs(max_sum - curr))

    min_sum = min(min_sum, curr)
    max_sum = max(max_sum, curr)

print(answer)