def star(n):
    if n == 3:
        return([['***'], ['* *'], ['***']])
    else:
        byeol = []
        ref = star(n//3)
        for i in range(n//3):
            byeol.append(ref[i] * 3)
        for i in range(n//3):
            temp = [' ' * (n//3)]
            byeol.append(ref[i] + temp + ref[i])
        for i in range(n//3):
            byeol.append(ref[i] * 3)
        return byeol

N = int(input())
ans = star(N)
for i in range(N):
    print(''.join(ans[i]))
