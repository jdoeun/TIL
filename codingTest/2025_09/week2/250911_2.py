N, M = map(int, input().split())
r, c, d = map(int, input().split())
room_list = [list(map(int, input().split())) for _ in range(N)]


# 북 동 남 서 순서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, d):
    global count

    # 1번 문항
    if 0 <= x < N and 0 <= y < M and room_list[x][y] == 0:
        room_list[x][y] = 2
        count += 1

    # 3번 문항
    for _ in range(4):
        d = (d + 3) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < M and room_list[nx][ny] == 0:
            dfs(nx, ny, d)
            return

    # 2번 문항 (후진 시에는 네번 돌아서 제자리로 온 d 기준)
    else:
        bx = x - dx[d]
        by = y - dy[d]

        if 0 <= bx < N and 0 <= by <= M and room_list[bx][by] != 1:
            dfs(bx, by, d)
        else:
            return

count = 0
dfs(r, c, d)
print(count)