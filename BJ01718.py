alphabet = 'abcdefghijklmnopqrstuvwxyz'
lst = []
for a in alphabet:
    lst.append(a)
ref = {}
for i, v in enumerate(lst):
    ref[v] = i+1

line = input()
password = input()
P = len(password)
ans = []

for i in range(len(line)):
    if line[i] == ' ':
        ans.append(' ')
    else:
        ans.append((ref.get(line[i])-ref.get(password[i % P])))

answer = ''
for i in range(len(line)):
    if ans[i] == ' ':
        answer += ' '
    elif ans[i] <= 0:
        for k, v in ref.items():
            if ans[i] + len(alphabet) == v:
                answer += k
                break
    else:
        for k, v in ref.items():
            if ans[i] == v:
                answer += k
                break

print(answer)
