from collections import deque

N = int(input())
cage = deque([1, 1, 1])

for i in range(N):
    cage.popleft()
    cage.append((cage[0] + cage[1] * 2) % 9901)

print(cage[2])
