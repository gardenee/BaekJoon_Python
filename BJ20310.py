S = input()
zero, one = S.count('0')//2, S.count('1')//2
ref = [True] * len(S)

for i in range(len(S)):
    if S[i] == '1':
        ref[i] = False
        one -= 1
    if not one: break

for i in range(len(S)-1, -1, -1):
    if S[i] == '0':
        ref[i] = False
        zero -= 1
    if not zero: break

answer = ''
for i in range(len(S)):
    if ref[i]: answer += S[i]

print(answer)
