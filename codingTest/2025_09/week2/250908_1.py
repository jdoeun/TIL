# BOJ: 2468 안전영역 BFS

import sys
sys.setrecursionlimit(100000) #??

N = int(input())
height = []
for i in range(N):
    height.append(list(map(int, input().split())))

max_height = height[0][0]

for i in range(N):
    if max(height[i]) >= max_height:
        max_height = max(height[i])


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, h):

    if x < 0 or x >= N or y < 0 or y >= N:
        return

    if visited[x][y]:
        return

    if height[x][y] <= h:
        return

    visited[x][y] = True

    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        dfs(next_x, next_y, h)

count_list = []
for h in range(0, max_height+1):
    visited = [[False]*N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and height[i][j] > h:
                dfs(i, j, h)
                count += 1

    count_list.append(count)

print(max(count_list))