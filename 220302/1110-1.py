m = input()
n = str(m)
a = '0'
answer = 0

if int(m) == 0:
    answer = 1
else:
    while int(m) != int(a):
        if int(n) < 10:
            a = n[-1] + n[-1]
            n = a
            answer += 1
        else:
            z = int(n[0]) + int(n[1])
            if z >= 10:
                z = str(z)[1]
            else:
                z = str(z)
            a = y + z
            n = a
            answer += 1

print(answer)