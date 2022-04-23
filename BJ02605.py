N = int(input())
ord = []
for i in range(1, N+1):
    ord.append(i)
lst = list(map(int, input().split()))

for i in range(N):
    n = lst[i]
    if n != 0:
        temp = ord.pop(i)
        ord.insert(i-n, temp)

print(' '.join(map(str, ord)))
