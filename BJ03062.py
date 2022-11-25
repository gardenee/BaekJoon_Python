from sys import stdin

for _ in range(int(input())):
    num = stdin.readline().rstrip()
    num = str(int(num) + int(num[::-1]))

    answer = "YES"
    for i in range((len(num)+1)//2):
        if num[i] != num[-i-1]:
            answer = "NO"
            break

    print(answer)
