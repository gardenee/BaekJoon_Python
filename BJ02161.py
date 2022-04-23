N = int(input())
cards = []
for i in range(N):
    cards.append(str(i+1))
ans = []

for _ in range(N-1):
    ans.append(cards.pop(0))
    cards.append(cards.pop(0))
ans.append(cards[0])

print(' '.join(ans))
