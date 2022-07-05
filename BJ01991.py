N = int(input())
tree = dict()

for _ in range(N):
    p, c1, c2 = input().split()
    tree[p] = [c1, c2]


#preorder
def preorder(node):
    temp = tree.get(node)
    print(node, end="")
    for i in range(len(temp)):
        if temp[i] != ".": preorder(temp[i])
preorder("A")
print()


#inorder
def inorder(node):
    temp = tree.get(node)
    for i in range(len(temp)):
        if i == 1: print(node, end="")
        if temp[i] != ".": inorder(temp[i])

inorder("A")
print()


#postorder
def postorder(node):
    temp = tree.get(node)
    for i in range(len(temp)):
        if temp[i] != ".": postorder(temp[i])
    print(node, end="")

postorder("A")
print()
