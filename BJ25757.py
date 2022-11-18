from sys import stdin

N, game = input().split()
waiting = set()

for _ in range(int(N)):
    player = stdin.readline().rstrip()
    waiting.add(player)

if game == "Y":
    print(len(waiting))
elif game == "F":
    print(len(waiting)//2)
elif game == "O":
    print(len(waiting)//3)
