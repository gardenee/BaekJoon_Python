from sys import stdin
import heapq

N = int(input())
card = []
for _ in range(N):
    heapq.heappush(card, int(stdin.readline()))

answer = 0
while len(card) > 1:
    c1 = heapq.heappop(card)
    c2 = heapq.heappop(card)
    answer += c1 + c2
    heapq.heappush(card, c1+c2)

print(answer)
