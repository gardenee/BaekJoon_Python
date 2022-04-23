ans = 0
ipt = []

for i in range(8):
    ipt.append(input())

for m in range(8):
    for n in range(8):
        if m%2 ==1:
            if n%2 == 1 and ipt[m][n] == 'F':
                ans += 1
        else:
            if n%2 == 0 and ipt[m][n] == 'F':
                ans += 1

print(ans)
