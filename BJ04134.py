from sys import stdin
from sys import stdout

for _ in range(int(input())):
    n = int(stdin.readline())
    answer = n
    flag = True

    if n == 2 or n == 3:
        answer += 1
        flag = False
    elif n == 0 or n == 1:
        answer = 3
        flag = False

    while flag:
        for i in range(2, int(answer ** 0.5) + 1):
            if answer % i == 0:
                break
            if i == int(answer ** 0.5):
                flag = False
        answer += 1

    stdout.write(str(answer-1) + "\n")
