# bfs
from collections import deque

def solution(numbers, target):
    queue = deque([(0, 0)])  # (현재 값, 인덱스) 초기값
    count = 0

    while queue:
        current, index = queue.popleft()  # 큐에서 현재 상태를 가져옴

        # 모든 숫자를 다 사용했을 때 결과 확인
        if index == len(numbers):
            if current == target:
                count += 1

        else:
            queue.append((current + numbers[index], index + 1))
            queue.append((current - numbers[index], index + 1))

    return count


# dfs
def solution(numbers, target):
    def dfs(index, current):  # current는 지금까지 계산된 값

        # 모든 숫자를 탐색한 경우
        if index == len(numbers):
            # 현재 값이 target과 같으면 경우의 수로 추가
            return 1 if current == target else 0

        return dfs(index + 1, current + numbers[index]) + dfs(index + 1, current - numbers[index])

    return dfs(0, 0)