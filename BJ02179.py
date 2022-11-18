from sys import stdin


def compare(root, new_word):
    cnt, prefix, prev, flag = 0, "", root, True
    for letter in new_word:
        if flag and letter in prev.son_values:
            prefix += letter
            cnt += 1
            for son in prev.sons:
                if son.value == letter:
                    prev = son
                    break
        else:
            flag = False
            curr = Node(letter, prev)
            prev.son_values.add(letter)
            prev.sons.add(curr)
            prev = curr

    return cnt, prefix


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.son_values = set()
        self.sons = set()
        self.parent = parent


N = int(input())
prefix, cnt = "", 0

ipt = []
tree = dict()
root = Node("dummy", None)

for i in range(N):
    word = stdin.readline().rstrip()
    ipt.append(word)
    num, pre = compare(root, word)
    if num > cnt:
        cnt = num
        prefix = pre

answer_cnt = 0
for word in ipt:
    if word[:cnt] == prefix:
        print(word)
        answer_cnt += 1
    if answer_cnt == 2:
        break
