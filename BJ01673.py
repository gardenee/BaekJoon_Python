while True:
    try:
        k, n = map(int, input().split())
        ans = 0
        while k >= n:
            ans += (k//n) * n
            k = k % n + k//n
        ans += k
        print(ans)
    except:
        break
