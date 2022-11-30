import sys
input = sys.stdin.readline
print = sys.stdout.write

for _ in range(int(input())):
    n = int(input())
    answer = 0
    visited = [False] * n
    choice = list(map(int, input().split()))

    for i in range(n):
        if choice[i] == i+1:
            visited[i] = True

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        check = dict()
        check[i] = 0
        prev, idx = i, 1

        while True:
            next = choice[prev]-1

            if next in check:
                answer += check[next]
                break
            if visited[next]:
                answer += idx
                break

            visited[next] = True
            check[next] = idx
            prev = next
            idx += 1

    print(str(answer) + "\n")
