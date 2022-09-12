from sys import stdin

ipt = list(input())
N = int(input())

ans = ""
ref = dict()

for i in range(len(ipt)):
    curr = ipt[i]
    ref.setdefault(curr, [])
    ref[curr].append(i)

for _ in range(N):
    cmd = list(stdin.readline().replace('\n', '').split())
    temp = 0
    if ref.get(cmd[0]):
        search = ref[cmd[0]]
        for s in search:
            if s > int(cmd[2]):
                break;
            if s >= int(cmd[1]):
                temp += 1
    ans += str(temp) + "\n"

print(ans)
