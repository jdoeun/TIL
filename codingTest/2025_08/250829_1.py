# 프로그래머스 : 짝지어 제거하기

def solution(s):
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()

        else:
            stack.append(ch)

    return 1 if not stack else 0