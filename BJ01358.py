W, H, X, Y, P = map(int, input().split())
ans = 0

for p in range(P):
    x, y = map(int, input().split())
    if x >= X and x <= (X+W) and y >= Y and y <= (Y+H):
        ans += 1
    elif H**2 / 4 >= (X-x)**2 + (Y+H/2-y)**2:
        ans += 1
    elif H**2 / 4 >= (X+W-x)**2 + (Y+H/2-y)**2:
        ans += 1

print(ans)
