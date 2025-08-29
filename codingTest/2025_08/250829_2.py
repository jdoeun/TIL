# 프로그래머스 : 피보나치 수

def solution(n):
    # DP로 해결
    fib = [0, 1]

    for i in range(2, n + 1):
        fib.append((fib[i - 1] + fib[i - 2]) % 1234567)

    return fib[-1]