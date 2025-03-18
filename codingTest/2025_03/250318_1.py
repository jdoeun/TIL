# programmers: 구명보트

from collections import deque


def solution(people, limit):
    answer = 0
    people.sort()
    queue = deque(people)

    while queue:
        if len(queue) == 1:
            answer += 1
            break

        if queue[0] + queue[-1] <= limit:  # 가장가볍 + 가장무겁
            queue.popleft()
            queue.pop()

        else:  # 무거운사람
            queue.pop()

        answer += 1

    return answer