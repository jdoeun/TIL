# programmers: 예상 대진표

def solution(n, a, b):
    round_num = 0

    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        round_num += 1

    return round_num