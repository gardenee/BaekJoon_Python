class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class SingleLinkedlist:
    def __init__(self):
        self.head = ListNode('dummy', None)

    def get_node(self, num):
        n = 1
        curr_node = self.head
        while n <= num:
            curr_node = curr_node.next
            n += 1
        return curr_node


N = int(input())

SLL = SingleLinkedlist()
curr = SLL.head

for i in range(1, N+1):
    new_node = ListNode(i, None)
    curr.next = new_node
    curr = new_node

change = list(map(int, input().split()))
for i in range(1, N+1):
    n = change[i-1]
    if n != 0:
        curr = SLL.get_node(i)
        temp = SLL.get_node(i-n-1)
        if curr.next:
            SLL.get_node(i-1).next = curr.next
        curr.next = temp.next
        temp.next = curr

curr = SLL.head.next
for _ in range(N):
    print(curr.val, end=" ")
    curr = curr.next
