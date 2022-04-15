N = int(input())

towers = list(map(int, input().split()))
answer = []

ref = {}
ref[0] = 0
for n, v in enumerate(towers):
    ref[v] = n+1

for _ in range(N):
    temp = towers.pop()
    stack = towers.copy()
    num = 0
    while stack:
        n = stack.pop()
        if n > temp:
            num = n
            break
    answer.append(ref[num])

for _ in range(N):
    print(answer.pop(), end=" ")
