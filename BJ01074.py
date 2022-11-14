N, r, c = map(int, input().split())
answer = 0


def divide(x, y, n):
    global answer
    if n == 1:
        print(answer)
        return

    n //= 2
    if x <= r < x+n and y <= c < y+n:
        divide(x, y, n)
    elif x <= r < x+n and y+n <= c < y+2*n:
        answer += n ** 2
        divide(x, y+n, n)
    elif x+n <= r < x+2*n and y <= c < y+n:
        answer += 2 * n ** 2
        divide(x+n, y, n)
    elif x+n <= r < x+2*n and y+n <= c < y+2*n:
        answer += 3 * n ** 2
        divide(x+n, y+n, n)


divide(0, 0, 2**N)
