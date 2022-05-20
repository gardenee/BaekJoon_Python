from sys import stdin

ipt = list(input())
N = int(input())

ans = ""
arr = [[0] * 26 for _ in range(len(ipt))]

for i in range(len(ipt)):
    arr[i][ord(ipt[i])-97] = 1
    if i != 0:
        for j in range(26):
            arr[i][j] += arr[i-1][j]

for _ in range(N):
    cmd = stdin.readline().split()
    if int(cmd[1]) != 0:
        print(arr[int(cmd[2])][ord(cmd[0])-97] - arr[int(cmd[1])-1][ord(cmd[0])-97])
    else:
        print(arr[int(cmd[2])][ord(cmd[0])-97])
