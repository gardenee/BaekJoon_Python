N = int(input())
visited = [False] * N
route = []

search = [N]
while N != 1 and True:
    curr = [0] * N
    temp = set()
    for c in search:
        if c % 3 == 0 and not visited[c//3]:
            temp.add(c//3)
            curr[c//3] = c
        if c % 2 == 0 and not visited[c//2]:
            temp.add(c//2)
            curr[c//2] = c
        if not visited[c-1]:
            temp.add(c-1)
            curr[c-1] = c

    route.append(curr)
    search = list(temp)
    if 1 in temp:
        break

if N == 1:
    print(0)
    print(1)
else:
    print(len(route))
    answer = [1]
    curr = 1
    for r in route[::-1]:
        curr = r[curr]
        answer.append(curr)
    for x in answer[::-1]:
        print(x, end=" ")
