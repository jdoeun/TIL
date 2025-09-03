# BOJ: 2606 바이러스

# dfs
computer_count = int(input())
pair_count = int(input())

graph = [[False] * (computer_count+1) for _ in range(computer_count+1)]

for i in range(pair_count):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited = [False] * (computer_count+1)

def dfs(V, count):
    visited[V] = True
    count += 1
    for i in range(1, computer_count+1):
        if not visited[i] and graph[V][i] == True:
            count = dfs(i, count) # 카운트 값 업데이트 필요

    return count

print(dfs(1, 0)-1) # 자기자신 제외