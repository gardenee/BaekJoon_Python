from sys import stdin


def gcs(a, b):
    temp = b
    b = a % b
    a = temp
    if b==0: return a
    else: return gcs(a, b)


T = int(input())
for _ in range(T):
    a, b = map(int, stdin.readline().split())
    A = max(a, b)
    B = min(a, b)

    print(A * B // gcs(A, B))
