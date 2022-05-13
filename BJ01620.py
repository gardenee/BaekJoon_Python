from sys import stdin

N, M = map(int, input().split())
aton = dict()
ntoa = dict()

for i in range(N):
    curr = stdin.readline().replace('\n', '')
    aton.setdefault(curr, i+1)
    ntoa.setdefault(i+1, curr)

for _ in range(M):
    curr = stdin.readline().replace('\n', '')
    try:
        print(ntoa[int(curr)])
    except:
        print(aton[curr])
