import math
x1, y1, x2, y2, x3, y3 = map(int, input().split())
if x1 == x2 == x3 or y1 == y2 == y3 or (y1 != y2 and y1 != y3 and (x1-x2)/(y1-y2) == (x1-x3)/(y1-y3)) or\
        (x1 != x3 and x1 != x2 and (y1-y2)/(x1-x2) == (y1-y3)/(x1-x3)):
    print(-1)
else:
    p1 = [x3-x1+x2, y3-y1+y2]
    p2 = [x3-x2+x1, y3-y2+y1]
    p3 = [x1+x2-x3, y1+y2-y3]
    ans = []
    ans.append((math.sqrt((p1[0]-x2)**2 + (p1[1]-y2)**2)+math.sqrt((p1[0]-x3)**2 + (p1[1]-y3)**2))*2)
    ans.append((math.sqrt((p2[0]-x1)**2 + (p2[1]-y1)**2)+math.sqrt((p2[0]-x3)**2 + (p2[1]-y3)**2))*2)
    ans.append((math.sqrt((p3[0]-x2)**2 + (p3[1]-y2)**2)+math.sqrt((p3[0]-x1)**2 + (p3[1]-y1)**2))*2)
    print(max(ans)-min(ans))

