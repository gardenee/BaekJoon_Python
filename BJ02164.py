cards = []
N = int(input())

for i in range(1, N+1):
    cards.append(i)

i = -1
for _ in range(N-1):
    i += 2
    temp = cards[i]
    cards.append(temp)

print(cards.pop())
