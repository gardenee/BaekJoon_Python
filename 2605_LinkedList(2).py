class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def get_Node(num):
    n = 1
    me = head
    while n <= num:
        me = me.next
        n += 1
    return me

N = int(input())
head = ListNode('dummy', None)
node = head
for i in range(1, N+1):
    node_new = ListNode(i, None)
    node.next = node_new
    node = node_new

change = list(map(int, input().split()))
for i in range(1, N+1):
    n = change[i-1]
    if n != 0:
        now = get_Node(i)
        temp = get_Node(i-n-1)
        if now.next:
            get_Node(i-1).next = now.next
        now.next = temp.next
        temp.next = now

ans = []
print_node = head.next
for _ in range(N):
    ans.append(str(print_node.val))
    print_node = print_node.next

print(' '.join(ans))
