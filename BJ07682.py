from sys import stdin


def check(n):
    global bingo
    if ipt[n] == "X":
        bingo[0] += 1
    elif ipt[n] == "O":
        bingo[1] += 1


while True:
    ipt = stdin.readline().rstrip()
    if ipt == "end": break

    answer = True
    X, O = ipt.count("X"), ipt.count("O")

    if X != O and X != O+1:
        answer = False

    bingo = [0, 0]
    for i in range(3):
        if ipt[i*3] == ipt[i*3+1] == ipt[i*3+2]:
            check(i*3)
        if ipt[i] == ipt[i+3] == ipt[i+6]:
            check(i)
    if ipt[0] == ipt[4] == ipt[8]:
        check(0)
    if ipt[2] == ipt[4] == ipt[6]:
        check(2)

    if bingo[0] * bingo[1] != 0:
        answer = False
    if bingo[0] == bingo[1] == 0 and X+O != 9:
        answer = False
    if bingo[1] != 0 and X > O:
        answer = False
    if bingo[0] != 0 and X == O:
        answer = False

    if answer: print("valid")
    else: print("invalid")
