from collections import deque
N, K = map(int, input().split())

answer = []
alive = []
people = deque([])
for i in range(N):
    people.append(i+1)

T = 1; n = 0
while n < N:
    if len(people) == 0:
        people = deque(alive)
        alive = []

    if T < K:
        alive.append(people.popleft())
        T += 1
    else:
        answer.append(str(people.popleft()))
        T = 1; n += 1

print("<" + ", ".join(answer) + ">")
