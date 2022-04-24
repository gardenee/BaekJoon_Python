from sys import stdin

class Que:
    def __init__(self):
        self.que = []
        self.size = 0

    def push(self, X):
        self.que.append(X)
        self.size += 1

    def pop(self):
        if self.que:
            self.size -= 1
            return(self.que.pop(0))
        else:
            return -1

    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.que:
            return self.que[0]
        else:
            return -1

    def back(self):
        if self.que:
            return self.que[-1]
        else:
            return -1


myQue = Que()
for _ in range(int(input())):
    command = list(stdin.readline().rstrip().split())
    if command[0] == "push":
        myQue.push(int(command[1]))
    elif command[0] == "pop":
        print(myQue.pop())
    elif command[0] == "size":
        print(myQue.size)
    elif command[0] == "empty":
        print(myQue.empty())
    elif command[0] == "front":
        print(myQue.front())
    elif command[0] == "back":
        print(myQue.back())
