zeminies = list(map(int, input().split()))
gullivers = list(map(int, input().split()))
winning = False
away, home = 0, 0

for i in range(9):
    away += zeminies[i]
    if not winning and away > home:
        winning = True

    home += gullivers[i]

if winning and home > away:
    print("Yes")
else:
    print("No")
