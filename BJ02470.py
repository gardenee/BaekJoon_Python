N = int(input())
reagents = list(map(int, input().split()))
reagents.sort()

answer = [-1, -1]
mixed = 2000000001

for i in range(N-1):
    curr = reagents[i]
    start, end = i+1, N

    while start < end:
        mid = (start+end)//2
        mix = reagents[mid] + curr

        if abs(mix) < mixed:
            mixed = abs(mix)
            answer = [curr, reagents[mid]]

        if mix >= 0:
            end = mid
        else:
            start = mid+1

print(*answer)
