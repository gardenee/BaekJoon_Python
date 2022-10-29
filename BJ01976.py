N = int(input())
M = int(input())
parents = [i for i in range(N+1)]


def find_parents(a):
    global parents
    if a == parents[a]:
        return a
    parents[a] = find_parents(parents[a])
    return parents[a]


def union(a, b):
    parents[find_parents(b)] = find_parents(a)


for i in range(N):
    ipt = list(map(int, input().split()))
    for j in range(N):
        if ipt[j] == 1 and i < j:
            union(i+1, j+1)

answer = 'YES'
find = list(map(int, input().split()))
for i in range(len(find)-1):
    if find_parents(find[i]) != find_parents(find[i+1]):
        answer = 'NO'
        break

print(answer)
