from sys import stdin
from collections import deque

N = int(input())
deq = deque([])
answer = []

for _ in range(N):
    ipt = list(map(int, stdin.readline().split()))
    cmd = ipt[0]

    if cmd == 1:
        deq.appendleft(str(ipt[1]))
    elif cmd == 2:
        deq.append(str(ipt[1]))
    elif cmd == 3:
        if deq: answer.append(str(deq.popleft()))
        else: answer.append("-1")
    elif cmd == 4:
        if deq: answer.append(str(deq.pop()))
        else: answer.append("-1")
    elif cmd == 5:
        answer.append(str(len(deq)))
    elif cmd == 6:
        if deq: answer.append("0")
        else: answer.append("1")
    elif cmd == 7:
        if deq: answer.append(str(deq[0]))
        else: answer.append("-1")
    elif cmd == 8:
        if deq: answer.append(str(deq[-1]))
        else: answer.append("-1")

print('\n'.join(answer))
