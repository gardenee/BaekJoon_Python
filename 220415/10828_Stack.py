from sys import stdin

class stack:
    def __init__(self):
        self.stk = []
        self.num = 0

    def push(self, X):
        self.stk.append(X)
        self.num += 1

    def pop(self):
        if self.stk:
            print(self.stk.pop())
            self.num -= 1
        else:
            print(-1)

    def size(self):
        print(self.num)

    def empty(self):
        if self.stk:
            print(0)
        else:
            print(1)

    def top(self):
        if self.stk:
            temp = self.stk.pop()
            print(temp)
            self.stk.append(temp)
        else:
            print(-1)

S = stack()
for _ in range(int(input())):
    command = list(stdin.readline().split())
    if command[0] == 'push':
        S.push(int(command[1]))
    elif command[0] == 'pop':
        S.pop()
    elif command[0] == 'size':
        S.size()
    elif command[0] == 'empty':
        S.empty()
    elif command[0] == 'top':
        S.top()
