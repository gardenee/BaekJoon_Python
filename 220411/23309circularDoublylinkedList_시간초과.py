from sys import stdin

class ListNode:
    def __init__(self, val, prev, next):
      self.val = val
      self.prev = prev
      self.next = next

def find_station(node, st_num):
    while True:
        if node.val == st_num:
            break
        else:
            node = node.next
    return node

N, M = map(int, input().split())
station = list(map(int, input().split()))
head = ListNode(station[0], None, None)
head.next = head
head.prev = head
curr = head
for i in range(1, N):
    new_station = ListNode(station[i], None, None)
    new_station.next = curr.next
    new_station.next.prev = new_station
    curr.next = new_station
    new_station.prev = curr
    curr = new_station

for _ in range(M):
    info = list(stdin.readline().split())
    curr = find_station(curr, int(info[1]))
    if info[0] == 'BN':
        print(curr.next.val)
        new = ListNode(int(info[2]), None, None)
        new.next = curr.next
        new.next.prev = new
        curr.next = new
        new.prev = curr
    elif info[0] == 'BP':
        print(curr.prev.val)
        new = ListNode(int(info[2]), None, None)
        new.prev = curr.prev
        new.prev.next = new
        curr.prev = new
        new.next = curr
    elif info[0] == 'CN':
        print(curr.next.val)
        curr.next = curr.next.next
        curr.next.prev = curr
    elif info[0] == 'CP':
        print(curr.prev.val)
        curr.prev = curr.prev.prev
        curr.prev.next = curr
