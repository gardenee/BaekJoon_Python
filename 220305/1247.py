import sys

for _ in range(3):
    plus = 0
    for _ in range(int(input())):
        plus += int(sys.stdin.readline())
    if plus == 0:
        print('0')
    elif plus > 0:
        print('+')
    else:
        print('-')