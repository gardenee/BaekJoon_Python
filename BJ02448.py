N = int(input())
n = N//3


def star(x):
    if x == 1:
        return ["  *  ", " * * ", "*****"]
    else:
        new = []
        prev = star(x//2)
        for i in range(3 * (x//2)):
            new.append(" " * (3 * (x//2)) + prev[i] + " " * (3 * (x//2)))
        for i in range(3 * (x//2)):
            new.append(prev[i] + " " + prev[i])
        return new


star = star(n)
for l in star:
    print(l)
