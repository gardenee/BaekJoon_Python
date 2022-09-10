def recursion(s, l, r, n):
    n += 1
    if l >= r: return 1, n
    elif s[l] != s[r]:  return 0, n
    else: return recursion(s, l+1, r-1, n)


def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 0)


N = int(input())
for _ in range(N):
    a, b = isPalindrome(input())
    print(a, b)
