ref = ["Equilateral", "Isosceles", "Scalene", "Invalid"]

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break

    max_d = max(a, max(b, c))

    if 2*max_d >= a+b+c:
        print(ref[3])
    elif a == b == c:
        print(ref[0])
    elif a == b or a == c or b == c:
        print(ref[1])
    else:
        print(ref[2])
