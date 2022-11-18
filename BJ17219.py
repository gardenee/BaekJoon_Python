from sys import stdin

N, M = map(int, input().split())
note = dict()

for _ in range(N):
    domain, password = stdin.readline().rstrip().split()
    note[domain] = password

for _ in range(M):
    domain = stdin.readline().rstrip()
    print(note[domain])
