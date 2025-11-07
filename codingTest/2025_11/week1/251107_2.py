# BOJ: 1699 제곱수의 합

n = int(input())
dp = [0] * (n + 1)

for i in range(1, n+1):
    dp[i] = i # 1을 계속 더하는 경우
    j = 1

    while j * j <= i:
        dp[i] = min(dp[i], dp[i - j*j] + 1)
        j += 1


print(dp[n])