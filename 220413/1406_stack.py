from sys import stdin

head = list(input())
tail = []

for _ in range(int(input())):
    command = list(stdin.readline().split())
    if command[0] == 'L':
        if head:
            tail.append(head.pop())
    elif command[0] == 'D':
        if tail:
            head.append(tail.pop())
    elif command[0] == 'B':
        if head:
            head.pop()
    else:
        head.append(command[1])

answer = head + tail[::-1]
print(''.join(answer))
