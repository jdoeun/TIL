# programmers: 아이템 줍기 bfs
# 어려움. 나중에 꼭 다시 풀기. 최단거리 문제

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    graph = [[-1 for _ in range(102)] for _ in range(102)]
    visited = [[1 for _ in range(102)] for _ in range(102)]

    direction = [(0, -1), (1, 0), (0, 1), (-1, 0)] # 컴퓨터 좌표계의 위, 오른쪽, 아래쪽, 왼쪽

    queue = deque()

    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                # x1, x2, y1, y2는 테두리이므로 제외하고 내부만 0으로 채움
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0

                # 다른 직사각형의 내부가 아니면서 테두리일 때 1로 채움
                elif graph[i][j] != 0:
                    graph[i][j] = 1

    # 반복문을 마치면 테두리는 1, 내부는 0, 외부는 -1이 됨

    # 캐릭터와 아이템의 좌표도 2배씩 늘린다
    cx, cy, ix, iy = 2*characterX, 2*characterY, 2*itemX, 2*itemY

    queue.append((cx, cy))

    while queue:
        x, y = queue.popleft()

        if x == ix and y == iy:
            # 답을 반환할 때 2로 나누어 반환
            answer = (visited[x][y] - 1) // 2 # -1 하던 안하던 동일함
            return answer

        for k in range(4):
            nx, ny = x + direction[k][0], y + direction[k][1]

            # 해당 좌표가 직사각형의 테두리인지 확인 + 해당 좌표가 아직 방문되지 않았는지 확인
            if graph[nx][ny] == 1 and visited[nx][ny] == 1:
                visited[nx][ny] += visited[x][y]
                queue.append((nx, ny))