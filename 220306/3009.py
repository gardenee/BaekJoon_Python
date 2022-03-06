lst_x = []
lst_y = []
x=0
y=0

for _ in range(3):
    x, y = (map(int, input().split()))
    lst_x.append(x)
    lst_y.append(y)

if lst_x.count(max(lst_x)) == 1:
    x = max(lst_x)
else:
    x = min(lst_x)

if lst_y.count(max(lst_y)) == 1:
    y = max(lst_y)
else:
    y = min(lst_y)

print(x, y)