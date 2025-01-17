# programmers: 네트워크 dfs

from collections import deque

def solution(n, computers):
    visited = [0] * n
    count = 0

    def bfs(v):

        queue = deque([v])  # append 따로 안써도 됨
        visited[v] = 1

        while queue:
            current = queue.popleft()
            for i in range(n):
                if computers[current][i] == 1 and visited[i] == 0:
                    visited[i] = 1
                    queue.append(i)

    # 모든 노드를 순회하며 bfs 수행
    for i in range(n):
        if visited[i] == 0:
            count += 1
            bfs(i)

    return count