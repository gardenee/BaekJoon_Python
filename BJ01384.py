num = 0

while True:
    if num != 0:
        print('')

    N = int(input())
    if N == 0:
        break

    num += 1
    print('Group', num)

    dic = {}
    names = []
    for _ in range(N):
        temp = list(input().split())
        name = temp.pop(0)
        names.append(name)
        dic.setdefault(name, [])
        for i in range(N-1):
            dic[name].append(temp[i])

    ans = {}
    for n in range(N):
        for i in range(N-1):
            if dic[names[n]][i] == 'N':
                j = i
                if not(names[n] in ans):
                    ans[names[n]] = []
                ans[names[n]].append(names[n-i-1])


    if ans == {}:
        print('Nobody was nasty')
    else:
        for i in ans:
            for j in ans[i]:
                print(j, 'was nasty about', i)

