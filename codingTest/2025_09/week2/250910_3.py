# BOJ: 9205 맥주 마시면서 걸어가기 BFS

from collections import deque

def bfs(home, stores, rock):

    queue = deque([home])
    visited = [False] * len(stores)

    while queue:
        x, y = queue.popleft()
        if [x, y] == rock:
            print("happy")
            return

        for i in range(len(stores)):
            if not visited[i]:
                next_x, next_y = stores[i]

                if abs(x - next_x) + abs(y - next_y) <= 1000:
                    queue.append((next_x, next_y))
                    visited[i] = True

    print("sad")

t = int(input()) # 테스트 케이스 개수

for _ in range(t):
    n = int(input())
    home = list(map(int, input().split()))
    stores = [list(map(int, input().split())) for _ in range(n)]
    rock = list(map(int, input().split()))
    stores.append(rock)

    bfs(tuple(home), stores, rock)