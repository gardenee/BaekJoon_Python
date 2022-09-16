def find_parents(x):
    global parents
    if parents[x] == x:
        print(x)
        return x
    return find_parents(parents[x])


def union(x, y):
    global parents
    x = find_parents(x)
    y = find_parents(y)
    parents[y] = x


N = int(input())
star = []
distance = dict()

for i in range(N):
    curr = list(map(float, input().split()))
    star.append(curr)
    for j in range(i):
        d = pow(star[j][0]-curr[0], 2)+pow(star[j][1]-curr[1], 2)
        distance.setdefault(d, [])
        distance[d].append([j, i])

key = list(distance.keys())
key.sort()

parents = [n for n in range(N)]
cnt = 0
answer = 0

for d in key:
    for dot in distance[d]:
        if find_parents(dot[0]) != find_parents(dot[1]):
            union(find_parents(dot[0]), find_parents(dot[1]))
            answer += d ** 0.5
            cnt += 1
        if cnt == N-1:
            break
    if cnt == N-1:
        break

print(round(answer, 2))
