from sys import stdin

while True:
    line = list(stdin.readline().rstrip())
    stack = []
    T = 0

    if line == ["."]:
        break

    while line:
        temp = line.pop()
        if temp == ')':
            stack.append(temp)
        elif temp == ']':
            stack.append(temp)
        elif temp == '(':
            if stack:
                pair = stack.pop()
                if pair != ')':
                    T = 1
                    break
            else:
                T = 1
                break
        elif temp == '[':
            if stack:
                pair = stack.pop()
                if pair != ']':
                    T = 1
                    break
            else:
                T = 1
                break

    if stack == [] and T == 0:
        print('yes')
    else:
        print('no')
