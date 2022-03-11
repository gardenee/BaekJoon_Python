while True:
    lst = list(map(int, input().split()))
    if lst == [0]:
        break
    ans = 1
    for _ in range(lst.pop(0)):
        ans *= lst.pop(0)
        ans -= lst.pop(0)
    print(ans)
        