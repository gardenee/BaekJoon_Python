def hanoi(n, b, c):
    if n == 1:
        print(b, c)
    else:
        hanoi(n-1, b, 6-b-c)
        print(b, c)
        hanoi(n-1, 6-b-c, c)

a = int(input())
print(2**a - 1)
hanoi(a, 1, 3)
