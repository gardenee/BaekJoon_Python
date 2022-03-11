A, B = map(int, input().split())

def location(x):
    if x % 4 == 0:
        return [x//4-1, 4]
    else:
        return [x//4, x % 4]

a = location(A); b = location(B)
print(abs(a[0]-b[0])+abs(a[1]-b[1]))
