N = int(input())
n = []
for _ in range(N):
    n.append(int(input()))

if n[1] * 2 == n[0] + n[2]:
    d = n[1] - n[0]
    print(n[-1] + d)
else:
    r = n[1] / n[0]
    print(int(n[-1] * r))
