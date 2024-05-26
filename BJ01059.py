L = int(input())
S = set(list(map(int, input().split())))
n = int(input())

left, right = n, n
x, y = 0, 0

while left > 0 and left not in S:
    x += 1
    left -= 1

while right not in S:
    y += 1
    right += 1

if n in S:
    print(0)
else:
    print(x * y - 1)
