# programmers: 피보나치 수

def solution(n):
    if n == 0:
        answer = 0

    elif n == 1:
        answer = 1

    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    answer = fib[n] % 1234567

    return answer