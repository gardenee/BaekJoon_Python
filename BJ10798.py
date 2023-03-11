board = [input() for _ in range(5)]

answer = ""
for i in range(15):
    for j in range(5):
        if len(board[j]) > i:
            answer += board[j][i]

print(answer)
