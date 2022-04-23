for _ in range(int(input())):
    a, b = map(int, input().split())
    if a * b == 0 and a != b:
        print('no')
    else:
        print('yes')
