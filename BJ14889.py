def dfs(lst1):
    global answer
    if len(lst1) == N//2:
        lst2 = []
        for i in range(N):
            if i not in lst1:
                lst2.append(i)
        start = 0
        link = 0
        for i in range(N//2-1):
            for j in range(i+1, N//2):
                start += plus[lst1[i]][lst1[j]]
                start += plus[lst1[j]][lst1[i]]
                link += plus[lst2[i]][lst2[j]]
                link += plus[lst2[j]][lst2[i]]
        answer = min(answer, abs(start-link))
        return

    for i in range(N):
        if not lst1 or i > lst1[-1]:
            lst1.append(i)
            dfs(lst1)
            lst1.pop()


N = int(input())
answer = 90000
plus = []
for _ in range(N):
    plus.append(list(map(int, input().split())))

dfs([])
print(answer)
