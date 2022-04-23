N, Q = map(int, input().split())
scores = []
for _ in range(N):
    scores.append(int(input()))

for _ in range(Q):
    q = int(input())
    time = 0
    for i in range(len(scores)):
        time += scores[i]
        if time > q:
            print(i+1)
            break
        elif time == q:
            print(i+2)
            break
