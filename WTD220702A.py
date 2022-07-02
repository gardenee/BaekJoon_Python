N, K = map(int, input().split())
monster = list(map(int, input().split()))
people = list(map(int, input().split()))
answer = 0


def dfs(ans, hp, damage, visited):
    global answer
    if hp < 0: return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            damage += monster[i]
            hp -= damage
            ans += people[i]

            if hp >= 0 and ans > answer:
                answer = ans

            dfs(ans, hp, damage, visited)

            visited[i] = False
            hp += damage
            damage -= monster[i]
            ans -= people[i]


dfs(0, K, 0, [False] * N)
print(answer)
