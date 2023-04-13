N, M = map(int, input().split())
lectures = list(map(int, input().split()))

answer = 100000000

start, end = max(lectures), sum(lectures)+1
while start < end:
    mid = (start + end)//2

    cnt, video = 1, 0
    for lecture in lectures:
        if video + lecture > mid:
            cnt += 1
            video = lecture
        else:
            video += lecture

    if cnt > M:
        start = mid+1
    else:
        answer = min(answer, mid)
        end = mid

print(answer)
