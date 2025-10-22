# BOJ: 9095 1,2,3 더하기

T = int(input())
test = [int(input()) for i in range(T)]

for t in test:
    dp = [0] * (max(4, t+1))

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    if t <= 3:
        print(dp[t])
        continue

    for i in range(4, t+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

    print(dp[t])

