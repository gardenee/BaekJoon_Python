N, M = map(int, input().split())
box = list(map(int, input().split()))
book = list(map(int, input().split()))
ans = 0

while book != []:
    if book[0] < box[0]:
        box[0] -= book.pop(0)
    elif book[0] == box[0]:
        book.pop(0)
        box.pop(0)
    else:
        ans += box.pop(0)

if box != []:
    for b in box:
        ans += b

print(ans)
