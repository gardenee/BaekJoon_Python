from sys import stdin
from collections import deque

for _ in range(int(input())):
    cmd = stdin.readline().rstrip()
    n = int(stdin.readline())
    arr = list(stdin.readline().replace("\n", "").replace("[", "").replace("]", "").replace(",", " ").split(" "))
    arr = deque(arr)

    ans = 1
    front = 1
    for c in cmd:
        if c == "R":
            front *= -1
        elif c == "D":
            if n == 0:
                ans = 0
                print("error")
                break
            else:
                if front == 1:
                    arr.popleft()
                elif front == -1:
                    arr.pop()
                n -= 1

    if ans == 1:
        if front == 1:
            print("[" + ",".join(arr) + "]")
        else:
            arr = list(arr)
            arr = arr[::-1]
            print("[" + ",".join(arr) + "]")
