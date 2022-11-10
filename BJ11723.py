from sys import stdin

S = set()

for _ in range(int(input())):
    cmd = stdin.readline().rstrip()
    if cmd == "empty":
        S = set()
        continue
    if cmd == "all":
        S = set([(i+1) for i in range(20)])
        continue

    cmd, x = cmd.split()
    x = int(x)

    if cmd == "add":
        S.add(x)
    elif cmd == "remove":
        if x in S:
            S.remove(x)
    elif cmd == "check":
        if x in S:
            print(1)
        else:
            print(0)
    elif cmd == "toggle":
        if x in S:
            S.remove(x)
        else:
            S.add(x)
