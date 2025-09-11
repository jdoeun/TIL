# BOJ: 14503 로봇 청소기 BFS

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room_list = [list(map(int, input().split())) for _ in range(N)]


# bfs
from collections import deque

# 북 동 남 서 순서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, direction):
    count = 0
    queue = deque([(x, y, direction)])

    while queue:
        x, y, d = queue.popleft()

        # 1번) 현재 위치가 청소되지 않았다면 청소
        if room_list[x][y] == 0:
            room_list[x][y] = 2 # 청소 완료 처리
            count += 1

        # 2번) 왼쪽 방향부터 탐색
        moved = False
        for _ in range(4):
            d = (d + 3) % 4 # 왼쪽 회전
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and room_list[nx][ny] == 0:
                queue.append((nx, ny, d))
                moved = True
                break

        # 3번) 네 방향 모두 청소할 곳이 없었다면 후진
        if not moved:
            bx, by = x - dx[d], y - dy[d]

            if 0 <= bx < N and 0 <= by < M and room_list[bx][by] != 1:
                queue.append((bx, by, d))
            else:
                break

    return count

print(bfs(r, c, d))

