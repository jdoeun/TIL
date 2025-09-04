# BOJ: 2178 미로탐색
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())

graph = []

for i in range(N):
    graph.append(list(map(int, input()))) # .split()은 공백 기준으로 입력받는데 여기서는 공백이 없음

queue = deque([(0, 0)])

while queue:
    x, y = queue.popleft()
    for i in range(4):
        next_x, next_y = x+dx[i], y+dy[i]
        if 0 <= next_x < N and 0 <= next_y < M:
            if graph[next_x][next_y] == 1:
                queue.append((next_x, next_y))
                graph[next_x][next_y] = graph[x][y] + 1

print(graph[N-1][M-1])