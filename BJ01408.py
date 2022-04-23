now = input()
start = input().replace(':', '')

if not start:
    print(now)
else:
    now = now.replace(':', '')
    now_s = int(now[:2]) * 3600 + int(now[2:4]) * 60 + int(now[4:])
    start_s = int(start[:2]) * 3600 + int(start[2:4]) * 60 + int(start[4:])
    if now_s < start_s :
        left = start_s - now_s
    else:
        left = start_s - now_s + 3600 * 24
    print('{0:02d}'.format(left//3600) + ':' + '{0:02d}'.format((left%3600)//60) + ':' +
               '{0:02d}'.format((left%3600)%60))

