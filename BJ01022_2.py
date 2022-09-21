r1, c1, r2, c2 = map(int, input().split())


def find(i, j):
    d = max(abs(i), abs(j))
    if d == 0:
        return 1

    value = (2*d - 1) ** 2
    if j == d:
        if i == d:
            value += 8*d
        else:
            value += d - i
    elif j == -d:
        value += 5*d + i
    elif i == -d:
        value += 3*d-j
    elif i == d:
        value += 7*d + j

    return value


length = [find(r1, c1), find(r1, c2), find(r2, c1), find(r2, c2)]
l = len(str(max(length)))

for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        print(str(find(i, j)).rjust(l, ' '), end=" ")
    print("\n", end="")
