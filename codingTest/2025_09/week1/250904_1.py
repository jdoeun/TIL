# BOJ: 2644 촌수계산

n = int(input())
start, target = map(int, input().split())
m = int(input())


graph = [[False] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

answer = -1

def dfs(V, depth):
    global answer
    visited[V] = True

    if V == target:
        answer = depth
        return

    for i in range(1, n+1):
        if not visited[i] and graph[V][i]:
            dfs(i, depth+1)

dfs(start, 0)
print(answer)
