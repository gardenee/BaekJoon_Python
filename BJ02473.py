N = int(input())

liquids = list(map(int, input().split()))
liquids.sort()

min_acidity = 3000000000
answer = []

for i in range(N-2):
    start, end = i+1, N-1

    while start < end:
        mix_three = liquids[i] + liquids[start] + liquids[end]

        if abs(mix_three) < min_acidity:
            answer = [liquids[i], liquids[start], liquids[end]]
            min_acidity = abs(mix_three)

        if mix_three < 0:
            start += 1
        elif mix_three == 0:
            break
        else:
            end -= 1

    if min_acidity == 0:
        break

print(*answer)
