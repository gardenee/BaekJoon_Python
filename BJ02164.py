cards = []
N = int(input())

for i in range(1, N+1):
    cards.append(i)

i = -1
last = N-1
while i+1 != last:
    last += 1
    i += 2
    temp = cards[i]
    cards.append(temp)
    print(cards)
    print("i", i, "last", last)

print(cards.pop())
