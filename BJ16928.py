from collections import deque

ladder, snake = map(int, input().split())
graph = [n for n in range(101)]

for _ in range(ladder + snake):
    x, y = map(int, input().split())
    graph[x] = y

visited = [0] * 2 + [10000] * 99
queue = deque([1])

while queue:
    curr = queue.popleft()

    if curr == 100:
        print(visited[100])
        break

    for dice in range(1, 7):
        if curr + dice > 100:
            continue

        next = graph[curr + dice]

        if visited[next] > visited[curr] + 1:
            visited[next] = visited[curr] + 1
            queue.append(next)
