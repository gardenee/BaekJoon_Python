from sys import stdin

class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def push(self, X):
        self.queue.append(X)
        self.size += 1

    def pop(self):
        if self.queue:
            self.size -= 1
            return(self.queue.pop(0))
        else:
            return -1

    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def back(self):
        if self.queue:
            return self.queue[-1]
        else:
            return -1


myQueue = Queue()
for _ in range(int(input())):
    command = list(stdin.readline().rstrip().split())
    if command[0] == "push":
        myQueue.push(int(command[1]))
    elif command[0] == "pop":
        print(myQueue.pop())
    elif command[0] == "size":
        print(myQueue.size)
    elif command[0] == "empty":
        print(myQueue.empty())
    elif command[0] == "front":
        print(myQueue.front())
    elif command[0] == "back":
        print(myQueue.back())
