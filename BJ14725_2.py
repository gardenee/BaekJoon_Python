class Node:
    def __init__(self, parent, value, d):
        self.parent = parent
        self.value = value
        self.sons = set()
        self.depth = d

    def getSons(self):
        temp = list(self.sons)

        values = []
        for son in temp:
            values.append(son.value)
        values.sort()

        return values

    def getSon(self, value):
        for son in self.sons:
            if son.value == value:
                return son
        return Node(self, value, self.depth+1)


root = Node("", "root", 0)

for _ in range(int(input())):
    ipt = list(input().split())
    K = int(ipt[0])
    currNode = root
    for i in range(1, K+1):
        prevNode = currNode
        currNode = prevNode.getSon(ipt[i])
        prevNode.sons.add(currNode)


def dfs(node):
    sons = node.getSons()
    depth = node.depth
    for son in sons:
        print("-" * depth * 2 + son)
        dfs(node.getSon(son))


dfs(root)
