ipt = list(input())
board = []
cnt = 0
for i in ipt:
    if i == '.':
        if cnt:
            board.append(cnt)
            cnt = 0
        board.append(i)
    else:
        cnt += 1
if cnt:
    board.append(cnt)

answer = ''
for b in board:
    if b == '.':
        answer += b
        continue
    if b % 2 == 1:
        answer = -1
        break
    while b > 0:
        if b == 2:
            answer += 'BB'
            break
        b -= 4
        answer += 'AAAA'

print(answer)
