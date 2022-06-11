N = int(input())
arr = [[0] * 11 for _ in range(N+2)]

for i in range(1, 10): arr[1][i] = 1
arr[2][1] = 2

for j in range(2, N+1):
    if j != 2: arr[j][1] = arr[j-1][2] + arr[j-2][1]
    for i in range(2, 10): arr[j][i] = arr[j-1][i-1] + arr[j-1][i+1]

print(sum(arr[N]) % 1000000000)
