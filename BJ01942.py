while True:
    try:
        s, e = input().split()
        s = s.replace(':', '')
        e = e.replace(':', '')
        ans = 0
        t = 0
        if int(e) > int(s):
            sH = int(s[:2]); sM = int(s[2:4]); sS = int(s[4:])
            while True:
                while sM < 60:
                    while sS < 60:
                        if int(e) < int(str('%02d' % sH) + str('%02d' % sM) + str('%02d' % sS)):
                            t = 1
                            break
                        if int(str('%02d' % sH) + str('%02d' % sM) + str('%02d' % sS)) % 3 == 0:
                            ans += 1
                        sS += 1
                    if t == 1:
                        break
                    sS = 0
                    sM += 1
                if t == 1:
                    break
                sM = 0
                sH += 1

        else:
            sS = 0; sM = 0; sH = 0
            while True:
                while sM < 60:
                    while sS < 60:
                        if int(e) < int(str('%02d' % sH) + str('%02d' % sM) + str('%02d' % sS)):
                            t = 1
                            break
                        if int(str('%02d' % sH) + str('%02d' % sM) + str('%02d' % sS)) % 3 == 0:
                            ans += 1
                        sS += 1
                    if t == 1:
                        break
                    sS = 0
                    sM += 1
                if t == 1:
                    break
                sM = 0
                sH += 1

            sH = int(s[:2]); sM = int(s[2:4]); sS = int(s[4:])
            while True:
                while sM < 60:
                    while sS < 60:
                        if int(str('%02d' % sH) + str('%02d' % sM) + str('%02d' % sS)) > 235959:
                            t = 2
                            break
                        if int(str('%02d' % sH) + str('%02d' % sM) + str('%02d' % sS)) % 3 == 0:
                            ans += 1
                        sS += 1
                    if t == 2:
                        break
                    sS = 0
                    sM += 1
                if t == 2:
                    break
                sM = 0
                sH += 1

        print(ans)

    except:
        break
