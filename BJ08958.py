def check(L):
    ans = 0
    for i in range(len(L)):
        temp = 0
        for n in range(i,-1,-1):
            if L[n] == 'O':
                temp += 1
            else:
                break
        ans += temp
    return ans

for _ in range(int(input())):
    lst = []
    c = str(input())
    for x in c:
        lst.append(x)
    print(check(lst))
