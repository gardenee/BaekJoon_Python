from sys import stdin

K = int(input())
answer = []

for _ in range(K):
    V, E = map(int, input().split())
    graph = dict()
    for _ in range(E):
        u, v = map(int, stdin.readline().split())
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)

    nodes = [0] * (V+1)
    is_binary = True

    for i in range(1, V+1):
        if nodes[i]:
            continue
        nodes[i] = 1
        stack = [i]
        while stack:
            node = stack.pop()
            current = nodes[node]
            if node not in graph.keys():
                break
            near = graph[node]
            for near_node in near:
                if nodes[near_node] == current:
                    is_binary = False
                    stack = []
                    break
                elif nodes[near_node] == 0:
                    nodes[near_node] = current * -1
                    stack.append(near_node)
        if not is_binary:
            break

    if is_binary:
        answer.append("YES")
    else:
        answer.append("NO")

print("\n".join(answer))
