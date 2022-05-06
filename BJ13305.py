N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

ans = 0
curr = price[0]
for i in range(N-1):
    if i == 0:
        ans += curr * distance[0]
    else:
        if price[i] < curr:
            curr = price[i]
        ans += curr * distance[i]

print(ans)
