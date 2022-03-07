def Rev(x):
    x2 = str(x)[::-1]
    return int(x2)

X, Y = map(int, input().split())
print(Rev(Rev(X)+Rev(Y)))