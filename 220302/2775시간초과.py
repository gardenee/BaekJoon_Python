def people(f, h):
    if f == 0:
        return h
    elif h == 1:
        return 1
    else:
        return people(f-1, h) + people(f, h-1)

for _ in range(int(input())):
    k = int(input())
    n = int(input())

    print(people(k, n))
