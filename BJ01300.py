N = int(input())
k = int(input())
arr = []

start, mid, end, cnt, answer, bool = 0, 0, N**2+1, 0, 0, False

while start < end:
    cnt = 0
    mid = (start + end)//2
    for i in range(N):
        if i+1 < mid:
            cnt += min(N, (mid-1)//(i+1))
    print("start", start , "end", end, "mid", mid, "cnt", cnt)

    if cnt <= k-1:
        start = mid+1
    else:
        end = mid

    if cnt == k-1:
        bool = True
        answer = mid
    elif not bool and cnt < k:
        answer = mid

print(answer)
