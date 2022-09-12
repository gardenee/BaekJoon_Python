stack1 = list(input())
stack2 = []
T = 0
n = 0
ans = 0

while stack1:
    temp = stack1.pop()
    if temp == ')':
        stack2.append(temp)
        n += 1
        T = 0
    elif temp == '(':
        stack2.pop()
        n -= 1
        if T == 0:
            ans += n
            T = 1
        else:
            ans += 1

print(ans)
