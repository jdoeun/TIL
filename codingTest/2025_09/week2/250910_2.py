# BOJ: 7569 토마토 BFS

M, N, H = map(int, input().split())

box = []
for i in range(H):
    layer = []
    for j in range(N):
        layer.append(list(map(int, input().split())))
    box.append(layer)

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

from collections import deque

queue = deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 1:
                queue.append((x, y, z))

while queue:
    x, y, z = queue.popleft()

    for i in range(6):
        next_x = x + dx[i]
        next_y = y + dy[i]
        next_z = z + dz[i]

        if 0 <= next_x < M and 0 <= next_y < N and 0 <= next_z < H:
            if  box[next_z][next_y][next_x] == 0:
                box[next_z][next_y][next_x] = box[z][y][x] + 1
                queue.append((next_x, next_y, next_z))

answer = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 0: # 모두 익지 못하는 상황
                print(-1)
                exit()
            answer = max(answer, box[z][y][x]) # 원래부터 다 익은 상태면 answer가 1이 됨

print(answer-1)
