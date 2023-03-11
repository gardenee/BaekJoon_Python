def find_gdc(a, b):
    if b == 0:
        return a
    tmp = a
    a = b
    b = tmp % b
    return find_gdc(a, b)


A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

A, B = A1 * B2 + A2 * B1, B1 * B2

gdc = find_gdc(max(A, B), min((A, B)))
print(A // gdc, B // gdc)
