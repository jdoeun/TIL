# programmers: 네트워크 dfs

def solution(n, computers):
    visited = [0] * n
    count = 0

    def dfs(v):

        visited[v] = 1
        for i in range(n):
            if computers[v][i] == 1 and visited[i] == 0:
                dfs(i)

    # 모든 노드를 순회하며 dfs 수행
    for i in range(n):
        if visited[i] == 0:
            count += 1
            dfs(i)

    return count
