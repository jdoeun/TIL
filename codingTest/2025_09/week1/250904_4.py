# BOJ: 2677 단지번호붙이기 BFS
from collections import deque

N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):

    global count

    if graph[x][y] == 0:
        return False

    q = deque([(x, y)])
    graph[x][y] = 0

    while q:
        x, y = q.popleft()
        count += 1

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
                continue

            if graph[next_x][next_y] == 1:
                q.append((next_x, next_y))
                graph[next_x][next_y] = 0

    return True

num = []
answer = 0
count = 0

for i in range(N):
    for j in range(N):
        if bfs(i, j) == True:
            answer += 1
            num.append(count)
            count = 0

print(answer)
num.sort()
for i in range(len(num)):
    print(num[i])


