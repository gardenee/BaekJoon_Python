from sys import stdin

def move(xy, c):
    if c == "R":
        return [xy[0]+1, xy[1]]
    elif c == "L":
        return [xy[0]-1, xy[1]]
    elif c == "B":
        return [xy[0], xy[1]+1]
    elif c == "T":
        return [xy[0], xy[1]-1]
    elif c == "RT":
        return [xy[0]+1, xy[1]-1]
    elif c == "LT":
        return [xy[0]-1, xy[1]-1]
    elif c == "RB":
        return [xy[0]+1, xy[1]+1]
    elif c == "LB":
        return [xy[0]-1, xy[1]+1]


start = list(input().split())
King = [ord(start[0][0])-65, 8 - int(start[0][1])]
Stone = [ord(start[1][0])-65, 8 - int(start[1][1])]

for _ in range(int(start[2])):
    cmd = stdin.readline().replace("\n", "").rstrip();
    Temp = King.copy()
    Temp = move(Temp, cmd)
    if (0 <= Temp[0] < 8) and (0 <= Temp[1] < 8):
        if Temp[0] == Stone[0] and Temp[1] == Stone[1]:
            Temp2 = Stone.copy()
            Temp2 = move(Temp2, cmd)
            if (0 <= Temp2[0] < 8) and (0 <= Temp2[1] < 8):
                Stone = Temp2
                King = Temp
        else:
            King = Temp


print(chr(65+King[0]) + str(8 - King[1]))
print(chr(65+Stone[0]) + str(8 - Stone[1]))
