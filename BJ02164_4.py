from queue import Queue

cards = Queue()
N = int(input())
for i in range(1, N+1):
    cards.put(i)

while cards.qsize() > 1:
    cards.get()
    temp = cards.get()
    cards.put(temp)

print(cards.get())
