N = int(input())
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
word = list(input())
for i in range(N):
    n = int(input())
    for j in range(len(word)):
        if word[j] == ABC[i]:
            word[j] = n


def calculate(cal, n2, n1):
    if cal == '+':
        return n1 + n2
    elif cal == '-':
        return n1 - n2
    elif cal == '*':
        return n1 * n2
    elif cal == '/':
        return n1 / n2


num = []

for w in word:
    temp = w
    if type(temp) == int:
        num.append(temp)
    else:
        num.append(calculate(temp, num.pop(), num.pop()))

print('%.2f' % (num[0]+0.00001))
