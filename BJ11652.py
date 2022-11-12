from sys import stdin

N = int(input())
count_cards = dict()

for _ in range(N):
    card = int(stdin.readline())
    count_cards[card] = count_cards.get(card, 0) + 1

answer, count_max = 0, 0
for card in count_cards.keys():
    card_cnt = count_cards[card]
    if card_cnt > count_max:
        count_max = card_cnt
        answer = card
    elif card_cnt == count_max:
        answer = min(answer, card)

print(answer)
