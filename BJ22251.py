N, K, P, X = map(int, input().split())

ref = [[1, 1, 1, 0, 1, 1, 1], [0, 0, 1, 0, 0, 0, 1], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1], [1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1]]
record = [[0] * 10 for _ in range(10)]

for i in range(10):
    for j in range(i, 10):
        cnt = 0
        for k in range(7):
            if ref[i][k] != ref[j][k]: cnt += 1
        record[i][j] = cnt
        record[j][i] = cnt

num = str(X).zfill(K)
answer = set()


def search(n, num, p):
    if n == K:
        if p != P and 0 < int(num) <= N:
            answer.add(num)
        return

    curr = int(num[n])
    for i in range(10):
        if record[curr][i] <= p:
            temp = num[:n] + str(i) + num[n+1:]
            search(n+1, temp, p-record[curr][i])


search(0, num, P)
print(len(answer))
