# programmers: 점프와 순간 이동

# 거꾸로 n에서 0까지 가는 걸 생각하면 됨
def solution(n):
    ans = 0

    while n > 0:
        if n % 2 == 0:
            n = n // 2

        else:
            # 점프는 제일 조금만 해야 함
            n = n - 1
            ans += 1

    return ans