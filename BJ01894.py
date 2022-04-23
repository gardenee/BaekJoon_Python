while True:
    try:
        x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())
        if x2 == x3 and y2 == y3:
            print('%.3f' % (x1 + x4 - x2), '%.3f' % (y1 + y4 - y2))
        elif x2 == x4 and y2 == y4:
            print('%.3f' % (x1 + x3 - x2), '%.3f' % (y1 + y3 - y2))
        elif x1 == x3 and y3 == y1:
            print('%.3f' % (x2 + x4 - x1), '%.3f' % (y2 + y4 - y1))
        elif x1 == x4 and y4 == y1:
            print('%.3f' % (x2 + x3 - x1), '%.3f' % (y2 + y3 - y1))

    except:
        break
