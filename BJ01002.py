for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        d = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
        if r1 + r2 < d:
            print(0)
        elif r1 + r2 == d:
            print(1)
        else:
            x = max(r1, r2)
            n = min(r1, r2)
            if d > x - n:
                print(2)
            elif d == x - n:
                print(1)
            else:
                print(0)
