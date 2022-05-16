from sys import stdin

N = int(input())
timeTable = dict()
ans = 0

times = []
for _ in range(N):
    times.append(list(map(int, stdin.readline().split())))

times.sort()

ans = 1
start = times[0][0]
end = times[0][1]
for i in range(1, len(times)):
    if end > times[i][1]:
        start = times[i][0]
        end = times[i][1]
    elif end <= times[i][0]:
        ans += 1
        start = times[i][0]
        end = times[i][1]

print(ans)
