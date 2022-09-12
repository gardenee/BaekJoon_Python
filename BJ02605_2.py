class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def get_Node(num):
    i = 0
    me = start
    while i < num:
        me = me.next
        i += 1
    return me

start = ListNode(0, None)
node = start
N = int(input())
for i in range(1, N+1):
    node_new = ListNode(i, None)
    node.next = node_new
    node = node_new

change = list(map(int, input().split()))
for i in range(1, N+1):
    for j in range(change[i-1]):
        now = get_Node(i-j)
        temp = get_Node(i-j-1)
        temp.next = now.next
        get_Node(i-j-2).next = now
        now.next = temp

ans = []
print_node = start.next
for _ in range(N):
    ans.append(str(print_node.val))
    print_node = print_node.next

print(' '.join(ans))
