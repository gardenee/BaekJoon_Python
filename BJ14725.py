N = int(input())

tree = dict()

for _ in range(N):
    ipt = input().split()
    K = int(ipt[0])
    parent = "root"
    for i in range(1, K+1):
        curr = ipt[i]
        tree.setdefault(parent, set())
        tree[parent].add(curr)

        if parent == "root":
            parent = curr
        else:
            parent += " " + curr


def dfs(parent, n):
    if parent not in tree:
        return

    sons = list(tree[parent])
    sons.sort()
    for son in sons:
        print("-" * n * 2 + son)
        if parent == "root":
            dfs(son, n+1)
        else:
            dfs(parent + " " + son, n+1)


dfs("root", 0)
