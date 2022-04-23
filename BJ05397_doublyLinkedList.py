from sys import stdin
class ListNode:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next

for _ in range(int(input())):
    head = ListNode('dummy', None, None)
    tail = ListNode('dummy', None, None)
    head.next = tail
    tail.prev = head
    curr = head

    log = stdin.readline().replace('\n', '')
    for l in log:
        if l == '>':
            if curr.next != tail:
                curr = curr.next
        elif l == '<':
            if curr != head:
                curr = curr.prev
        elif l == '-':
            if curr != head:
                curr = curr.prev
                curr.next = curr.next.next
                curr.next.prev = curr
        else:
            new_node = ListNode(l, None, None)
            new_node.next = curr.next
            new_node.next.prev = new_node
            curr.next = new_node
            new_node.prev = curr
            curr = new_node

    ans = []
    print_node = head.next
    while print_node.val != 'dummy':
        ans.append(print_node.val)
        print_node = print_node.next
    print(''.join(ans))
