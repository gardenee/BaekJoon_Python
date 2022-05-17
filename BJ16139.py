from sys import stdin

ipt = list(input())
N = int(input())

ans = ""
cmd = list(input().split())
sum = [0] * len(ipt)

for i in range(len(ipt)):
    if i != 0:
        sum[i] += sum[i-1]
    if ipt[i] == cmd[0]:
        sum[i] += 1

for i in range(N):
    if int(cmd[1]) == 0:
        ans += str(sum[int(cmd[2])]) + '\n'
    else:
        ans += str(sum[int(cmd[2])] - sum[int(cmd[1])-1]) + '\n'

    if i != N-1:
        cmd = list(stdin.readline().replace('\n', ' ').split())

print(ans)
