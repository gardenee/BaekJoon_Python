N = int(input())
reagents = list(map(int, input().split()))
answer = 2000000001
A, B = 0, 0

for i in range(N-1):
    curr = reagents[i]
    start, end = i+1, N
    while start < end:
        mid = (start+end)//2
        if abs(curr+reagents[mid]) < answer:
            answer = abs(curr+reagents[mid])
            A, B = curr, reagents[mid]
        if curr+reagents[mid] <= 0:
            start = mid+1
        else:
            end = mid

print(A, B)
