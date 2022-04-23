n = 0
life = 1

while True:
    life = 1
    o, w = map(int, input().split())
    if o == w == 0:
        break

    event, num = input().split()
    while True:
        if event == 'F':
            w += int(num)
        elif event == 'E':
            w -= int(num)
            if w <= 0:
                life = 0

        event, num = input().split()
        if event == '#' and num == '0':
            n += 1
            if life == 0:
                print(n, 'RIP')
            elif 0.5 * o < w < 2 * o:
                print(n, ':-)')
            else:
                print(n, ':-(')
            break
