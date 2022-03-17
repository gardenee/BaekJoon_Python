days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

x, y = map(int, input().split())
d = 0

for i in range(0, x-1):
    d += days[i]
d += y-1

print(day[d%7])
