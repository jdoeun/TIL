# BOJ: 5014 스타트링크
from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [-1] * (F+1) # -1로 모든 층 초기화
visited[S] = 0 # 버튼 수 카운트 위해 s층을 0으로 초기화

q = deque([S])

while q:

    x = q.popleft()
    if x == G:
        break

    for nx in (x+U, x-D):
        if 0 < nx <= F and visited[nx] == -1:
            q.append(nx)
            visited[nx] = visited[x] + 1

if visited[G] != -1:
    print(visited[G])
else:
    print("use the stairs")