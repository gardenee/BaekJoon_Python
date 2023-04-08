from sys import stdin

answer = 0
sent_emoticon = set()

for _ in range(int(input())):
    log = stdin.readline().strip()
    if log == 'ENTER':
        sent_emoticon = set()
    else:
        if log not in sent_emoticon:
            answer += 1
            sent_emoticon.add(log)

print(answer)
