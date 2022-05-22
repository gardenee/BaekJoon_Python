lst = list(map(int, input()))
lst.sort(reverse=True)

if lst[-1] != 0:
    print(-1)
elif sum(lst) % 3 != 0:
    print(-1)
else:
    for l in lst:
        print(l, end="")
