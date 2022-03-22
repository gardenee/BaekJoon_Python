N, S = input().split()
N = int(N)
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ref = {}
for i, a in enumerate(ABC):
    ref[a] = i

one = [0] * N
game = [0] * N
Set = [0] * N

for s in S:
    if one[ref[s]] == 3 and one.count(3) == 1 and max(one) == 3:
        game[ref[s]] += 1
        one = [0] * N
    elif one[ref[s]] == 4:
        game[ref[s]] += 1
        one = [0] * N
    elif 4 in one:
        for i in range(len(one)):
            if one[i] == 4:
                one[i] -= 1
    else:
        one[ref[s]] += 1

    if max(game) >= 6 and game.count(max(game)) == 1 and (not ((max(game)-1) in game)):
        if game.count(0) == N-1:
            Set[game.index(max(game))] += 2
        else:
            Set[game.index(max(game))] += 1
        game = [0] * N

    if max(Set) >= 3:
        break

print(ABC[Set.index(max(Set))])
