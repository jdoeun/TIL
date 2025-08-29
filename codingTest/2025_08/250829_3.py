# Programmers - 점프와 순간 이동

# n에서 0으로 거꾸로 가는걸 생각
def solution(n):
    ans = 0

    while n > 0:
        if n % 2 == 0:
            n = n // 2  # / 쓰면 실수 비교라 시간 더 오래 걸림

        else:
            n = n - 1
            ans += 1

    return ans