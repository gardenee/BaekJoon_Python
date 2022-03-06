for _ in range(int(input())):
    a = list(map(int, input().split()))
    n = a.pop(0)
    score = 0
    for i in a:
        score += i
    avg = score/n

    count = 0
    for i in a:
        if i > avg:
            count += 1

    print('{0:.3f}%'.format(round((count/len(a))*100,3)))
