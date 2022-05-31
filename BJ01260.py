from sys import stdin
from collections import deque
import sys
sys.setrecursionlimit(10000)

N, M, V = map(int, input().split())
edges = dict()

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    edges.setdefault(a, [])
    edges.setdefault(b, [])
    edges[a].append(b)
    edges[b].append(a)


def dfs(curr: int, stack: list, graph: dict, visited: set):
    if curr==-1: return
    print(curr, end=" ")
    visited.add(curr)
    if graph.get(curr):
        temp = graph[curr]
        temp.sort(reverse=True)
    else: temp = []
    for t in temp:
        if not (t in visited):
            stack.append(t)
    if not stack: curr = -1
    while stack:
        curr = stack.pop()
        if curr in visited: curr = -1
        else: break
    return dfs(curr, stack, graph, visited)


def bfs(curr: int, queue: deque, graph: dict, visited: set):
    if curr==-1: return
    print(curr, end=" ")
    visited.add(curr)

    if graph.get(curr):
        temp = graph[curr]
        temp.sort()
    else: temp = []
    for t in temp:
        if not (t in visited):
            queue.append(t)
    if not queue: curr = -1
    while queue:
        curr = queue.popleft()
        if curr in visited: curr = -1
        else: break
    return bfs(curr, queue, graph, visited)


dfs(V, list(), edges, set())
print()
bfs(V, deque(), edges, set())
