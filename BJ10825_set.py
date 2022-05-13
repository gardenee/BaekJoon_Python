N = int(input())
cards = set(map(int, input().split()))
M = int(input())
find = list(map(int, input().split()))

ans = cards.intersection(set(find))

for m in find:
    if m in ans:
        print(1, end=" ")
    else:
        print(0, end=" ")
