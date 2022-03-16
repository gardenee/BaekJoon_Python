alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for _ in range(int(input())):
    num = input()
    temp = 0
    for i in range(3):
        temp += alphabet.index(num[i]) * 26 ** (2-i)
    if abs(temp - int(num[4:])) <= 100:
        print('nice')
    else:
        print('not nice')
