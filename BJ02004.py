n, m = map(int, input().split())
x = min(m, n-m); y = max(m, n-m)

def div(n, m):
    count = 0
    while n > 0:
        count += n // m
        n //= m
    return count


cnt5 = div(n, 5) - div(x, 5) - div(y, 5)
cnt2 = div(n, 2) - div(x, 2) - div(y, 2)

print(min(cnt5, cnt2))
