n = 0
x = 0
y = 0

for i in range(1, 10):
    ipt = list(map(int, input().split()))
    n = max(n, max(ipt))
    if n in ipt:
        y = i
        x = ipt.index(n)+1

print(n)
print(y, x)
