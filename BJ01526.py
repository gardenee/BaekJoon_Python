N = str(input())
ans = ''
cnt = len(N)

for n in range(len(N)):
    if int(N[n]) > 7:
        ans += '7' * cnt
        break
    elif int(N[n]) == 7:
        ans += '7'
        cnt -= 1
    elif int(N[n]) == 4:
        ans += '4'
        cnt -= 1
    elif 4 < int(N[n]) < 7:
        ans += '4' + '7' * (cnt -1)
        break
    else:
        T = 0
        for i in range(n-1, -1, -1):
            if ans[i] == '7':
                ans = ans[:i] + '4' + '7' * (n-i-1+cnt)
                T = 1
                break
        if T == 0:
            ans = '7' * (len(N)-1)
        break

print(ans)
