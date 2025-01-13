n = int(input())
n_twin = int(input())

# 행렬 만들기
graph = [[0] * (n+1) for _ in range(n+1)]

for i in range(n_twin):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [0] * (n+1)

count = 0

# dfs
def dfs(v):
    global count # 전역 변수 쓰려면 명시해야 함
    visited[v] = 1
    for i in range(1, n + 1):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i)
            count = count + 1

dfs(1)
print(count)