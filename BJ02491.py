N = int(input())
arr = list(map(int, input().split()))
up = [1] * N
down = [1] * N

for i in range(1, N):
    if arr[i] >= arr[i-1]:
        up[i] = up[i-1] + 1
    if arr[i] <= arr[i-1]:
        down[i] = down[i-1] + 1

print(max(max(up), max(down)))
