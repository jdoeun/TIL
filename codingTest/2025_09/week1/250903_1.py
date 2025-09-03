#Boj 1260 DFS와 BFS

from collections import deque

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)


def dfs(V):
    visited1[V] = True
    print(V, end=" ")
    for i in range(1, N + 1):
        if graph[V][i] and not visited1[i]:
            dfs(i)


def bfs(V):
    queue = deque([V])
    visited2[V] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in range(1, N + 1):
            if graph[v][i] and not visited2[i]:
                queue.append(i)
                visited2[i] = True

dfs(V)
print()
bfs(V)
