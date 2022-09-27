N = int(input())
answer = 0
row = [0] * N


def possible(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i):
            return False
    return True


def search(n):
    global answer
    if n == N:
        answer += 1
        return
    for i in range(N):
        row[n] = i
        if possible(n):
            search(n+1)


search(0)
print(answer)
