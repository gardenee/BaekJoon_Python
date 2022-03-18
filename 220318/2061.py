K, L = map(int, input().split())
T = 0
k = 0
for i in range(2, L):
    if K % i == 0:
        T = 1
        k = i
        break

if T == 1:
    print('BAD', k)
else:
    print('GOOD')