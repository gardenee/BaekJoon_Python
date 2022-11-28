from sys import stdin


def find_parents(X):
    global gates
    if X == gates[X]:
        return X
    else:
        gates[X] = find_parents(gates[X])
        return find_parents(gates[X])


def union(X, Y):
    global gates
    gates[find_parents(Y)] = find_parents(X)


G = int(input())
P = int(input())
gates = [0] * (G+1)

answer = 0
for _ in range(P):
    g = int(stdin.readline())

    if gates[g]:
        g = find_parents(gates[g])-1
        if g == 0:
            break

    gates[g] = g
    if g < G-1 and gates[g+1]:
        union(find_parents(g), find_parents(g+1))
    if gates[g-1]:
        union(find_parents(g-1), find_parents(g))
    answer += 1

print(answer)
