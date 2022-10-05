from sys import stdin


class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def push(self, num):
        self.heap.append(num)
        self.up(self.size)
        self.size += 1

    def pop(self):
        if self.heap:
            rtn = self.heap[0]
            temp = self.heap.pop()
            if self.heap: self.heap[0] = temp
            self.size -= 1
            self.down(0)
            return rtn
        else:
            return 0

    def up(self, n):
        if n == 0 or self.heap[n] <= self.heap[(n-1)//2]:
            return
        else:
            self.heap[n], self.heap[(n-1)//2] = self.heap[(n-1)//2], self.heap[n]
            self.up((n-1)//2)

    def down(self, n):
        search = 2*n+1
        if search >= self.size:
            return
        right = 2*n+2
        if right < self.size and self.heap[search] < self.heap[right]:
            search = right
        if self.heap[search] <= self.heap[n]:
            return
        else:
            self.heap[search], self.heap[n] = self.heap[n], self.heap[search]
            self.down(search)


heap = Heap()
N = int(input())

for _ in range(N):
    n = int(stdin.readline())
    if n == 0: print(heap.pop())
    else: heap.push(n)
