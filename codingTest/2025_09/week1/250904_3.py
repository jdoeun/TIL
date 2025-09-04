# BOJ: 2677 단지번호붙이기 DFS

N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int, input()))) # map은 lazy 객체여서 리스트로 바꿔줘야 함

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):

    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            dfs(next_x, next_y)

        return True

    return False

num = []
count = 0
result = 0

for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            num.append(count)
            result += 1
            count = 0

print(result)
num.sort()

for i in range(len(num)):
    print(num[i])