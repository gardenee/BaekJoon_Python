from sys import stdin
T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count = 0
    for i in range(n):
        planet = list(map(int, stdin.readline().split()))
        if (x1-planet[0]) ** 2 + (y1-planet[1]) ** 2 < planet[2] ** 2 < (x2-planet[0]) ** 2 + (y2-planet[1]) ** 2:
            count += 1
        elif (x2-planet[0]) ** 2 + (y2-planet[1]) ** 2 < planet[2] ** 2 < (x1-planet[0]) ** 2 + (y1-planet[1]) ** 2:
            count += 1

    print(count)
