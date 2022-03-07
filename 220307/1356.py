N = int(input())
ref = 0

for n in range(len(str(N))-1):
    n1 = str(N)[:n+1]
    n2 = str(N)[n+1:]
    temp1 = 1
    temp2 = 1

    for i in n1:
        temp1 *= int(i)
    for i in n2:
        temp2 *= int(i)

    if temp1 == temp2:
        print('YES')
        ref = 1
        break


if ref == 0:
    print('NO')
