def gcd(a, b):
    a, b = b % a, a
    if a == 0:
        return b
    else:
        return gcd(a, b)


for _ in range(int(input())):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    if b % a == 0:
        print(b)
        continue
    x = gcd(a, b)
    print(a * (b//x))
