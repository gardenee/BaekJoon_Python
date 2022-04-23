N = int(input())
K = int(input())

arr_d = [1] * (N+1)
arr_d[0] = 0
arr_d[1] = 0
for i in range(2, N+1):
    if arr_d[i] == 1:
        for j in range(2*i, N+1, i):
            arr_d[j] = 0
D = []
for k in range(K+1, N+1):
    if arr_d[k] == 1:
        D.append(k)

arr_a = [1] * (N+1)
arr_a[0] = 0
for d in D:
    for n in range(d, N+1, d):
        arr_a[n] = 0

print(arr_a.count(1))
