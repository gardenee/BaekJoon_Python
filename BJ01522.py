ipt = input()
N = len(ipt)

cnt_a = ipt.count("a")
cnt_b = N - cnt_a

answer = 10001
if cnt_a == N:
    answer = 0

for i in range(N):
    if ipt[i] == "a":
        continue

    temp = cnt_b
    for j in range(cnt_b):
        if ipt[(N+i+j) % N] == "b":
            temp -= 1

    answer = min(answer, temp)

print(answer)
