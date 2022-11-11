N, target = int(input()), input()
answer = 0

ref = [0] * 26
for alphabet in target: ref[ord(alphabet)-65] += 1

for _ in range(N-1):
    record = ref.copy()
    word = input()
    for w in word:
        record[ord(w)-65] -= 1

    _sum, cnt = 0, 0
    for r in record:
        if abs(r) > 1:
            cnt = 100
            break

        _sum += r
        if r != 0: cnt += 1
        if cnt > 2:
            break
        if abs(_sum) > 1:
            cnt = 100
            break

    if cnt <= 1:
        answer += 1

print(answer)
