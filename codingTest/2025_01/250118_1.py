from collections import deque
# programmers: 단어 변환 bfs
# 최소 단계를 찾아야 하므로 bfs
def solution(begin, target, words):
    if target not in words:
        return 0

    return bfs(begin, target, words)


def bfs(begin, target, words):
    queue = deque()
    queue.append([begin, 0])

    while queue:
        now, step = queue.popleft()

        if now == target:
            return step

        for word in words:
            count = 0
            for i in range(len(now)):
                if now[i] != word[i]:
                    count += 1

            if count == 1:  # 알파벳 1개만 다를 경우 교체
                queue.append([word, step + 1])
