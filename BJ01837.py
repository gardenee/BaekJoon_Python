P, K = map(int, input().split())
T = 0
for i in range(2, K):
    if P % i == 0:
        print('BAD', i)
        T = 1
        break

if T == 0:
    print('GOOD')
