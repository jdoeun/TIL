# BOJ: 2573 빙산

N, M = map(int, input().split())
height_list = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

from collections import deque

def bfs():
    queue = deque()
    year = 0

    while True: # 구현
        visited = [[False] * M for _ in range(N)]
        bingsan_count = 0
        # 1) 빙산 개수를 세기 (bfs 부분)
        for i in range(N):
            for j in range(M):
                if height_list[i][j] > 0 and not visited[i][j]:
                    bingsan_count += 1

                    queue.append((i, j))
                    visited[i][j] = True

                    while queue:
                        x, y = queue.popleft()

                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]

                            if 0 <= nx < N and 0 <= ny < M:
                                if not visited[nx][ny] and height_list[nx][ny] > 0:
                                    queue.append((nx, ny))
                                    visited[nx][ny] = True

        # 2) 빙산 개수에 따라 year을 출력하거나, 구현 시작
        if bingsan_count >= 2:
            print(year)
            return
        elif bingsan_count == 0:
            print(0)
            return
        elif bingsan_count == 1:
            melt_list = [[0]*M for _ in range(N)]

            for i in range(N):
                for j in range(M):
                    if height_list[i][j] > 0:
                        zero_count = 0

                        for k in range(4):
                            nx = i + dx[k]
                            ny = j + dy[k]

                            if 0 <= nx < N and 0 <= ny < M and height_list[nx][ny] == 0:
                                zero_count += 1
                        # 얼마나 녹아야 하는지를 저장
                        melt_list[i][j] = zero_count

            for i in range(N):
                for j in range(M):
                    height_list[i][j] -= melt_list[i][j]

                    if height_list[i][j] < 0:
                        height_list[i][j] = 0

            year += 1

bfs()
