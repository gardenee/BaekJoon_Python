from sys import stdin

N = int(input())
ready = []
for i in range(N, 0, -1):
    ready.append(i)
stack = []
temp = 0
ans = ""

for i in range(N):
    curr = int(stdin.readline())
    if stack and stack[-1] == curr:
        stack.pop()
        ans += "-\n"
    elif curr in stack:
        print("NO")
        ans = "NO"
        break
    else:
        while temp != curr:
            temp = ready.pop()
            stack.append(temp)
            ans += "+\n"
        stack.pop()
        ans += "-\n"

if ans != "NO":
    print(ans)
