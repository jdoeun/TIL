# BOJ: 20055 컨베이어 벨트 위의 로봇

from collections import deque

n, k = map(int, input().split())
a = deque(map(int, input().split())) # 내구도 A1, A2, ... A2N
robot = deque([0] * n) # 벨트위에 있는 로봇
result = 0

while True:
    result += 1

    # 1. 벨트 회전한다.
    a.rotate(1) # 내구도 한 칸씩 회전 (마지막 -> 맨 앞으로)
    robot[-1] = 0 # 로봇이 내리는 위치(n-1)에 있으면 내려야 함
    robot.rotate(1) # 로봇 위치도 같이 회전
    robot[-1] = 0

    # 2. 로봇 이동하기. 이동하려는 칸에 로봇 x, 내구도 1이상 남아야함.
    # 파이썬 인덱스는 1~n -> 0~n-1
    for i in range(n-2, -1, -1): # n-1칸에는 로봇 절대 못 있음. 먼저 올라간 로봇부터 앞으로 이동
        if a[i+1] >= 1 and robot[i+1] == 0 and robot[i] == 1:
            robot[i+1] = 1
            robot[i] = 0
            a[i+1] -= 1

    robot[-1] = 0 # 내리는 위치에 도달한 로봇은 내려감

    # 3. 올리는 위치에 내구도 0 아니면 로봇 올리기 & 내구도 감소
    if a[0] != 0 and robot[0] != 1:
        robot[0] = 1
        a[0] -= 1

    # 4. 내구도 0인 칸 수가 k이상이면 종료
    if a.count(0) >= k:
        break

print(result)