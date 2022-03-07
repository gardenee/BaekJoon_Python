N, L, D = map(int, input().split())

time = 0
stat = 0

for _ in range(N-1):
    time += L
    for _ in range(5):
        if time % D == 0:
            print(time)
            stat = 1
            break
        time += 1
    if stat:
        break

if not stat:
    time = time + L
    if time % D == 0:
        print(time)
    else:
        m = time % D
        print(time + D - m)
