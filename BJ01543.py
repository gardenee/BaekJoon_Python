file = input()
search = input()

answer = 0
i, j, cnt, n, m = 0, 0, 0, len(file), len(search)

while i < n:
    if file[i] == search[j]:
        cnt += 1
        i += 1
        j += 1
    else:
        i -= cnt-1
        j = 0
        cnt = 0
    if cnt == m:
        answer += 1
        cnt = 0
        j = 0

print(answer)
