# BOJ: 14501 퇴사 dp

N = int(input())
timeTable = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    t, p = timeTable[i]

    if i + t <= N:
        dp[i] = max(p + dp[i+t], dp[i+1]) # dp[i]는 최대 수익. 마지막 날부터 거꾸로 계산
    else:
        dp[i] = dp[i+1]

print(dp[0])