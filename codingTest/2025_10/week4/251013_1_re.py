# BOJ: 20055 컨베이어 벨트 위의 로봇 복습

from collections import deque

n, k = map(int, input().split())
a = deque(map(int, input().split()))
robot = deque([0] * n)
result = 0

while True:
    result += 1

    # 1. 벨트 회전
    a.rotate(1)
    robot[-1] = 0
    robot.rotate(1)
    robot[-1] = 0

    # 2. 로봇 이동
    for i in range(n-2, -1, -1):
        if a[i+1] >= 1 and robot[i+1] == 0 and robot[i] == 1:
            robot[i+1] = 1
            robot[i] = 0
            a[i+1] -= 1

    # 3. 내구도 0 아니면 로봇 올림
    if a[0] != 0 and robot[0] != 1:
        robot[0] = 1
        a[0] -= 1

    # 4. 내구도 0인 칸 개수 K개 이상이면 종료
    if a.count(0) >= k:
        break

print(result)