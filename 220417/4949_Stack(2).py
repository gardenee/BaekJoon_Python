from sys import stdin

ref = dict()
ref['['] = ']'
ref['('] = ')'

while True:
    line = list(stdin.readline().rstrip())
    if line == ["."]:
        break

    stack = []
    T = 0

    while line:
        temp = line.pop()
        if temp == ')':
            stack.append(temp)
        elif temp == ']':
            stack.append(temp)
        elif temp == '(' or temp == '[':
            if stack:
                if ref[temp] != stack.pop():
                    T = 1
                    break
            else:
                T = 1
                break

    if stack == [] and T == 0:
        print('yes')
    else:
        print('no')
