time = str(input())
T = [int(time[0:2]), int(time[3:5]), int(time[6:8])]
T.sort()

if T[2] > 59 or T[0] < 0:
    print(0)
elif T[0] > 12 or T[2] < 1:
    print(0)
elif T[0] >= 1 and T[2] <= 12:
    print(6)
elif (T[0] < 1 and T[1] >= 1 and T[2] <= 12) or (T[0] >= 1 and T[1] <= 12 and T[2] > 12):
    print(4)
else:
    print(2)
