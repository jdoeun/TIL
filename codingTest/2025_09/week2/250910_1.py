# BOJ: 2468 안전영역 BFS

N = int(input())

height = []
for i in range(N):
    height.append(list(map(int, input().split())))

max_height = height[0][0]

for i in range(N):
    if max_height < max(height[i]):
        max_height = max(height[i])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

from collections import deque

def bfs(x, y, h):

    visited[x][y] = True
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x >= 0 and next_x < N and next_y >= 0 and next_y < N:
                if not visited[next_x][next_y] and height[x][y] > h:
                    queue.append((next_x, next_y))
                    visited[next_x][next_y] = True


count_list = []
for h in range(0, max_height + 1):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False and height[i][j] > h:
                bfs(i, j, h)
                count += 1

    count_list.append(count)

print(max(count_list))