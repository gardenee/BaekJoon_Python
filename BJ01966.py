from sys import stdin
from collections import deque

for _ in range(int(input())):
    N, M = map(int, stdin.readline().split())
    queue = list(map(int, stdin.readline().split()))
    target = M

    priority = queue.copy()
    priority.sort(reverse=True)

    queue = deque(queue)
    priority = deque(priority)

    curr = priority.popleft()
    ans = 0
    while True:
        temp = queue.popleft()
        if curr == temp:
            ans += 1
            if target == 0:
                break;
            else:
                curr = priority.popleft()
                target -= 1
        else:
            queue.append(temp)
            if target == 0:
                target = len(queue)-1
            else:
                target -= 1

    print(ans)
