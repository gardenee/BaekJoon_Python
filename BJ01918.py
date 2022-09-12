lst = list(input().rstrip())
stack = []
ans = ''
for l in lst:
    if l == '(':
        stack.append(l)
    elif l == ')':
        while True:
            temp = stack.pop()
            if temp == '(':
                break
            else:
                ans += temp
    elif l == '*' or l == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            ans += stack.pop()
        stack.append(l)
    elif l == '+' or l == '-':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.append(l)
    else:
        ans += l

while stack:
    ans += stack.pop()

print(ans)