N = int(input())
pillars = [0] * 1001

max_h, max_l, idx = 0, 0, 0
for i in range(N):
    L, H = map(int, input().split())
    pillars[L] = H
    if H > max_h:
        max_h = H
        idx = L
    if L > max_l:
        max_l = L

answer, prev = 0, 0
for i in range(idx+1):
    if pillars[i] > prev:
        prev = pillars[i]
    answer += prev

prev = 0
for i in range(max_l, idx, -1):
    if pillars[i] > prev:
        prev = pillars[i]
    answer += prev

print(answer)
