N = int(input())
reagents = list(map(int, input().split()))
answer = 2000000001
A, B = 0, 0

start, end = 0, N-1
while start < end:
    if abs(reagents[start] + reagents[end]) < answer:
        answer = abs(reagents[start] + reagents[end])
        A, B = reagents[start], reagents[end]
    if reagents[start] + reagents[end] < 0:
        start += 1
    else:
        end -= 1

print(A, B)
