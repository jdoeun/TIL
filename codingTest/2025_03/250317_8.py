# programmers: 다음 큰 숫자

def solution(n):
    n_count_one = bin(n).count('1')

    while True:
        n = n + 1

        if n_count_one == bin(n).count('1'):
            return n