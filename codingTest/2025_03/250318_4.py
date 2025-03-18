# programmers: 멀리 뛰기

# 피보나치와 동일 (점화식 확인)
def solution(n):
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        # 수가 커지니 미리 나눠주기
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567

    return dp[n]