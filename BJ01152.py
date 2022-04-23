a = str(input()).lstrip().rstrip()
ans = 1

if a == '':
    print(0)
else:
    for i in a:
        if i == ' ':
            ans += 1
    print(ans)
