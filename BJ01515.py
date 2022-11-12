N = input()

answer = 0
i = 0
curr = 0

while i < len(N):
    curr = N[i]
    i += 1
    answer = int(answer) + 1

    while curr not in str(answer):
        answer += 1

    answer = str(answer)
    idx = answer.index(curr)
    for j in range(idx+1, len(answer)):
        if i < len(N) and N[i] == answer[j]:
            i += 1

print(int(answer))
