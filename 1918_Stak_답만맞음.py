def parentheses(stk1, stk2):
    i = 0
    while i < len(stk1):
        curr = stk1[i]
        if curr == '(':
            temp = []
            j = 1
            while (i+j) < len(stk1):
                now = stk1[i+j]
                if now == '(':
                    stk2.append('(')
                    stk2 += temp
                    temp = []
                    j += 1
                elif now == ')':
                    while ('*' in temp) or ('/' in temp):
                        temp2 = []
                        mul_div(temp, temp2)
                        temp = temp2.copy()
                    while ('+' in temp) or ('-' in temp):
                        temp2 = []
                        plus_min(temp, temp2)
                        temp = temp2.copy()
                    stk2 += temp
                    break
                else:
                    temp.append(now)
                    j += 1
            i += j + 1
        elif curr == ')':
            stk2.append(')')
            i += 1
        else:
            stk2.append(curr)
            i += 1

def mul_div(stk1, stk2):
    i = 0
    N = len(stk1)
    while i < N:
        curr = stk1[i]
        if curr == '*' or curr == '/':
            stk2.append(stk2.pop() + stk1[i+1] + curr)
            i += 2
        else:
            stk2.append(curr)
            i += 1

def plus_min(stk1, stk2):
    i = 0
    N = len(stk1)
    while i < N:
        curr = stk1[i]
        if curr == '+' or curr == '-':
            stk2.append(stk2.pop() + stk1[i+1] + curr)
            i += 2
        else:
            stk2.append(curr)
            i += 1

stack1 = list(input())
stack2 = []
while '(' in stack1:
    parentheses(stack1, stack2)
    stack1 = stack2.copy()
    stack2 = []
mul_div(stack1, stack2)
stack1 = stack2.copy()
stack2 = []
plus_min(stack1, stack2)

for i in stack2:
    print(i, end='')
