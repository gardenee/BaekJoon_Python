n = 0
num = 0
N = int(input())
while True:
    num += 1
    if '666' in str(num):
        n += 1
        if N == n:
            print(num)
            break
