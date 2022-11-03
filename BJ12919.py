S, T = input(), input()
S2 = S[::-1]
answer = 0


def dfs(t):
    print(t)
    global answer
    if answer == 1: return

    if len(t) == len(S):
        if t == S:
            answer = 1
        return

    if t[-1] == 'A':
        dfs(t[:len(t)-1])
    if t[0] == 'B':
        dfs(t[1:][::-1])


dfs(T)
print(answer)
