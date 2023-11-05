import sys

N = int(input())
stack = []
for _ in range(N):
    cmd = sys.stdin.readline().split(" ")
    cmd_cd = int(cmd[0])

    if cmd_cd == 1:
        stack.append(int(cmd[1]))
    elif cmd_cd == 2:
        print(stack.pop() if stack else -1)
    elif cmd_cd == 3:
        print(len(stack))
    elif cmd_cd == 4:
        print(0 if stack else 1)
    elif cmd_cd == 5:
        print(stack[-1] if stack else -1)
    else: continue
