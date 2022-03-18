for _ in range(3):
    s, e = input().split()
    s = s.replace(':', '')
    e = e.replace(':', '')
    ans = 0
    sH = int(s[:2]); sM = int(s[2:4]); sS = int(s[4:])
    eH = int(e[:2]); eM = int(e[2:4]); eS = int(e[4:])
    while sH != eH or sM != eM or sS != eS:
        if int(str('%02d' % sH) + str('%02d' % sM) + str('%02d' % sS)) % 3 == 0:
            ans += 1
        sS += 1
        if sS == 60:
            sS = 0
            sM += 1
        if sM == 60:
            sM = 0
            sH += 1
        if sH == 24:
            sH = 0
    if int(str('%02d' % sH) + str('%02d' % sM) + str('%02d' % sS)) % 3 == 0:
            ans += 1
    print(ans)
