L = int(input())
word = input()
answer, r, M, d = 0, 31, 1234567891, 1

for w in word:
    a = ord(w) - 96
    answer += (a * d) % M
    answer %= M
    d *= r
    d %= M

print(answer)
