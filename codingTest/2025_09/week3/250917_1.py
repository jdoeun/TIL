# BOJ: 14889 스타트와 링크 백트레킹

import sys

input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
INF = 1e9
res = INF

# DFS
def dfs(L, idx): # L: 현재까지 팀 A에 뽑힌 사람 수, idx: 다음 탐색 시작 위치
    global res
    if L == N//2:
        A = 0
        B = 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A += board[i][j]
                elif not visited[i] and not visited[j]:
                    B += board[i][j]

        res = min(res, abs(A-B))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(L+1, i+1)
            visited[i] = False # 상태 복구

dfs(0, 0)
print(res)
