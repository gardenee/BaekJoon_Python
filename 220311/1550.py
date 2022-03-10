nums = '0123456789ABCDEF'
ans = 0

ipt = str(input())
L = len(ipt)
for i in range(L):
    ans += (16 ** (L - 1 - i)) * nums.index(ipt[i])

print(ans)
