
while 1:
    a = int(input())
    x = 0
    if a == 0:
        break
    for i in range(len(str(a))//2):
        if str(a)[i] != str(a)[-1-i]:
            x = 1
            break
    if x == 0:
        print('yes')
    else:
        print('no')
