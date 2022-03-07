for _ in range(int(input())):
    a, b = map(int, input().split())
    x = max(a, b)
    y = min(a, b)
    r = x % y

    if r == 0:
        gcd = y
        lcm = x
    else:
        while True:
            x = y
            y = r
            r = x % y
            if r == 0:
                gcd = y
                break
        lcm = (a*b)//gcd

    print(lcm, gcd)
