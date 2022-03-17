alphabet = 'abcdefghijklmnopqrstuvwxyz'
dic = {}
for a in alphabet:
    dic[a] = 0

word = input()
for l in word:
    dic[l] += 1

word = input()
for l in word:
    dic[l] -= 1

ans = 0
for k in dic:
    ans += abs(dic[k])

print(ans)
