from collections import deque
cards = []
N = int(input())

for i in range(1, N+1):
    cards.append(i)

dequeCards = deque(cards)
for _ in range(N-1):
    dequeCards.popleft()
    temp = dequeCards.popleft()
    dequeCards.append(temp)

print(dequeCards.pop())
