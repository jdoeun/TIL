# programmers: 올바른 괄호

from collections import deque


# 스택을 사용해야 함
def solution(s):
    answer = True

    stack = deque()

    for i in range(len(s)):
        if s[i] == "(":
            stack.append("(")

        elif s[i] == ")":
            if not stack:
                return False

            stack.pop()

    if len(stack) == 0:
        return True

    return False