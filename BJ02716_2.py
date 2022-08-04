T = int(input())
for _ in range(T):
    ipt = list(input())
    m = 0
    d = 0
    for i in ipt:
        if i == '[':
            d += 1
            m = max(m, d)
        elif i == ']':
            d -= 1

    print(2 ** m)
