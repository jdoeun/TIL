# BOJ: 21608 상어 초등학교

n = int(input())
students = []
for i in range(n**2):
    students.append(list(map(int, input().split())))

data = [[0] * n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for student in students:
    available = []

    for i in range(n):
        for j in range(n):
            if data[i][j] == 0:
                prefer, empty = 0, 0

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < n and 0 <= ny < n:
                        if data[nx][ny] in student[1:]:
                            prefer += 1
                        if data[nx][ny] == 0:
                            empty += 1

                available.append((i, j, prefer, empty))

    available.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))
    data[available[0][0]][available[0][1]] = student[0]

answer = 0
score = [0, 1, 10, 100, 1000]
students.sort()

for i in range(n):
    for j in range(n):
        count = 0

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] in students[data[i][j]-1]:
                    count += 1

        answer += score[count]

print(answer)