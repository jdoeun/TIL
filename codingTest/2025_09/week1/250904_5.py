# BOJ: 1697 숨바꼭질
from collections import deque

N, K = map(int, input().split())

def bfs():

    q = deque([N])

    while q:
        x = q.popleft()

        if x == K:
            return dist[x]

        for nx in (x+1, x-1, x*2):
            if 0 <= nx <= max  and not dist[nx]:
                dist[nx] = dist[x] + 1 # bfs는 레벨 단위 탐색이라 처음 방문이 곧 최단거리
                q.append(nx)

max = 10 ** 5
dist = [0] * (max+1)

print(bfs())