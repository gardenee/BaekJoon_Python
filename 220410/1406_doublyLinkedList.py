from sys import stdin

class ListNode:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next

head = ListNode('dummy', None, None)
Node_num = 0
curr = head

init = input()
for i in range(len(init)):
    node_new = ListNode(init[i], None, None)
    curr.next = node_new
    node_new.prev = curr
    curr = node_new
    Node_num += 1

N = int(input())
for _ in range(N):
    command = stdin.readline().replace('\n', '')
    if command == 'L':
        if curr.val != 'dummy':
            curr = curr.prev
    elif command == 'D':
        if curr.next:
            curr = curr.next
    elif command == 'B':
        if curr.val != 'dummy':
            curr = curr.prev
            if curr.next.next:
                curr.next = curr.next.next
                curr.next.prev = curr
            else:
                curr.next = None
            Node_num -= 1
    else:
        new_node = ListNode(command[-1], None, None)
        if curr.next:
            new_node.next = curr.next
            curr.next.prev = new_node
        curr.next = new_node
        new_node.prev = curr
        curr = new_node
        Node_num += 1
    print_node = head.next

print_node = head.next
for _ in range(Node_num):
    print(print_node.val, end='')
    print_node = print_node.next
