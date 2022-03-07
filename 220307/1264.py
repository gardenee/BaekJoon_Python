v = ['a', 'e', 'i', 'o', 'u']

while True:
    s = input().lower()
    ans = 0
    if s == '#':
        break
    else:
        for i in s:
            if i in v:
                ans += 1
    print(ans)
