N, K = map(int, input().split())
lst = list(map(int, input().split()))

checked = [0] * (100001)
p1, p2 = 0, 0

answer, cnt = 1, 1
checked[lst[0]] += 1

while p2 < N-1:
    p2 += 1
    while checked[lst[p2]] >= K:
        checked[lst[p1]] -= 1
        p1 += 1
        cnt -= 1
    cnt += 1
    checked[lst[p2]] += 1
    answer = max(answer, cnt)

print(answer)
