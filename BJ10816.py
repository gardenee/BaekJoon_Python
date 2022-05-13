N = int(input())
cards = list(map(int, input().split()))
count = dict()
for c in cards:
    count.setdefault(c, 0)
    count[c] += 1

M = int(input())
find = list(map(int, input().split()))
for f in find:
    if count.get(f):
        print(count[f], end=" ")
    else:
        print(0, end=" ")
