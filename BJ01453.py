N = int(input())
guests = list(map(int, input().split()))
ans = 0

arr = [0] * 101
for g in guests:
    if arr[g] == 0:
        arr[g] = 1
    else:
        ans += 1

print(ans)
