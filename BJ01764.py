from sys import stdin

N, M = map(int, input().split())
DJ = set()
for _ in range(N):
    DJ.add(stdin.readline().replace('\n', ''))

BJ = set()
for _ in range(M):
    BJ.add(stdin.readline().replace('\n', ''))

DBJ = DJ.intersection(BJ)
print(len(DBJ))

DBJ = list(DBJ)
DBJ.sort()
print('\n'.join(DBJ))
