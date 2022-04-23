N = int(input())
A = list(map(int, input().split()))
A2 = A.copy()
A2.sort()
P = [0] * len(A)

for i in range(len(A)):
    P[A.index(A2[i])] = str(i)
    A[A.index(A2[i])] = '*'

print(' '.join(P))
