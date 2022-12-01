code = list(map(int, list(input())))
N = len(code)

ref = [1, 1]
for i in range(2, N+1):
    ref.append(ref[-1] + ref[-2])

answer, cnt, prev = 1, 0, 0
for i in range(N):
    curr = code[i]

    if not cnt and curr == 0:
        answer = 0
        break

    if 1 <= curr <= 2:
        cnt += 1
        prev = curr
        continue

    if cnt:
        if curr == 0:
            answer *= ref[cnt-1]
        elif (prev == 2 and curr <= 6) or prev == 1:
            answer *= ref[cnt+1]
        answer %= 1000000

    cnt = 0
    prev = curr

if cnt:
    answer *= ref[cnt]

print(answer % 1000000)
