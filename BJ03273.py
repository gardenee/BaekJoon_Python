n = int(input())
p = list(map(int, input().split()))
p.sort()
x = int(input())

answer = 0
i, j = 0, n-1

while i < j:
    if p[i] + p[j] == x:
        answer += 1

    if p[i] + p[j] <= x:
        i += 1
    elif p[i] + p[j] > x:
        j -= 1

print(answer)
