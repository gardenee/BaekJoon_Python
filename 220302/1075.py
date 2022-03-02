N = str(input())
F = int(input())

front = N[:-2]
ans = ''

for n in range(10):
    if ans != '':
        break
    for m in range(10):
        if int(front + str(n) + str(m)) % F == 0:
            ans += str(n) + str(m)
            break

print(ans)

