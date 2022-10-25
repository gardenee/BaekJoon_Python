N = int(input())
friends = [list(input()) for _ in range(N)]
answer = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if friends[i][j] == "Y":
            answer[i][j] = 1
            for n in range(N):
                if friends[j][n] == "Y" and n != i:
                    answer[i][n] = 1

rtn = 0
for i in range(N):
    rtn = max(rtn, sum(answer[i]))

print(rtn)
