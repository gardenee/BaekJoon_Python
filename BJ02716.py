import copy
from sys import stdin


def gcd(a, b):
    if min(a,b) == 0:
        return max(a, b)
    return gcd(min(a, b), max(a, b) % min(a, b))


def lcd(a, b):
    g = gcd(a, b)
    if max(a, b) == g:
        return g
    else:
        return a * b // g


T = int(input())

for _ in range(T):
    ipt = list(stdin.readline().replace("\n", ""))
    tree = [0] * 26
    tree[0] = [0]

    d = -1
    curr = 0
    for i in ipt:
        if i == '[':
            d += 1
            if d != 25 and not tree[d+1]:
                tree[d+1] = list()

            if d != 0:
                curr = curr * 2 + 1

            if d != 25 and curr*2+1 in tree[d+1]:
                curr = (max(tree[d+1])-1)//2 + 1

            tree[d+1].append(curr*2+1)
            tree[d+1].append(curr*2+2)

        elif i == ']':
            d -= 1
            curr = (curr-1) // 2

    if 0 in tree:
        tree = tree[:tree.index(0)]
    monkey = copy.deepcopy(tree)

    for d in range(len(tree)-1, -1, -1):
        for n in range(len(tree[d])):
            node = tree[d][n]
            if d != len(tree)-1 and node*2+1 in tree[d+1]:
                monkey[d][n] = 0

            if d == len(tree)-1:
                monkey[d][n] = 1
            elif node*2+1 in tree[d+1]:
                idx = tree[d+1].index(node*2+1)
                l_child = monkey[d+1][idx]
                r_child = monkey[d+1][idx+1]
                monkey[d][n] = lcd(l_child, r_child) * 2
            else:
                monkey[d][n] = 1

    print(monkey[0][0])
