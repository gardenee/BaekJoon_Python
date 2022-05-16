from sys import stdin
from collections import deque

deq = deque([])

for _ in range(int(input())):
    cmd = stdin.readline().split()

    if cmd[0] == 'push_front':
        deq.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        deq.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(deq))
    elif cmd[0] == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if deq:
            temp = deq.popleft()
            print(temp)
            deq.appendleft(temp)
        else:
            print(-1)
    elif cmd[0] == 'back':
        if deq:
            temp = deq.pop()
            print(temp)
            deq.append(temp)
        else:
            print(-1)
