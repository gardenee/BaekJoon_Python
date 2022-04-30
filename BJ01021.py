from collections import deque
N, M = map(int, input().split())
queue = deque()
for i in range(1, N+1):
    queue.append(i)
find = list(map(int, input().split()))

count = 0
i = 0
while (i < M):
    temp = queue.popleft();
    findNow = find[i]
    if temp == findNow:
        i += 1
    else:
        if queue.index(findNow) < (N-i)//2:
            queue.append(temp)
        else:
            queue.appendleft(temp)
            queue.appendleft(queue.pop())
        count += 1

print(count)
