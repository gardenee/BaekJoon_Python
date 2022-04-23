from sys import stdin

for _ in range(int(input())):
    stack1 = list(stdin.readline())
    stack2 = []
    T = 0
    while stack1:
        temp = stack1.pop()
        if temp == '(':
            if stack2:
                stack2.pop()
            else:
                T = 1
                break
        elif temp == ')':
            stack2.append(temp)

    if T == 0 and stack2 == []:
        print('YES')
    else:
        print('NO')
