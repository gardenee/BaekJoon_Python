import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
note = set()
deleted = set()

for _ in range(N):
    note.add(input().rstrip())

for _ in range(M):
    keywords = list(input().rstrip().split(','))
    for keyword in keywords:
        if keyword in note:
            deleted.add(keyword)
    print(str(len(note)-len(deleted)) + "\n")
