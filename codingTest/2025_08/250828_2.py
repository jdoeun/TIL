# programmers: 숫자의 표현

def solution(n):
    answer = 0

    for i in range(1, n + 1):
        hap = 0
        for j in range(i, n + 1):
            hap += j

            if hap == n:
                answer += 1
            elif hap > n:
                break

    return answer