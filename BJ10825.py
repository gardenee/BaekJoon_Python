N = int(input())
cards = list(map(int, input().split()))
ref = dict()
for c in cards:
    ref.setdefault(c, 1)

M = int(input())
find = list(map(int, input().split()))
for f in find:
    if ref.get(f) == 1:
        print(1, end=" ")
    else:
        print(0, end=" ")
