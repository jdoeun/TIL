# 제곱수? : 16 이면 약수 1 2 4 8 16
# 25 : 1 5 25
# 제곱근이면 sqrt = n ** (1/2) 사용 가능!
def solution(n):
    for i in range(1, n + 1):
        if (n % i == 0) and (i * i == n):
            return (i + 1) * (i + 1)

    return -1