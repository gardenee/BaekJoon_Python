def find_gdc(a, b):
    if b == 0:
        return a
    tmp = a
    a = b
    b = tmp % b
    return find_gdc(a, b)


A, B = map(int, input().split())
gdc = find_gdc(max(A, B), min(A, B))

print(A * B // gdc)
