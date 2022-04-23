ans = [0]*26
alphabet = list('abcdefghijklmnopqrstuvwxyz')

word = input()
for l in word:
    ans[alphabet.index(l)] += 1

answer = ''
for i in ans:
    answer += str(i)
    answer += ' '

print(answer.rstrip())
