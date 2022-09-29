N, L = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

answer = 1
prev = lst[0]
for l in lst:
    if l - prev >= L:
        answer += 1
        prev = l

print(answer)
