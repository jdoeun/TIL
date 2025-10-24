# BOJ: 2156 포도주 시식

n = int(input())
drink = [int(input()) for _ in range(n)]

if n == 1:
    print(drink[0])

elif n == 2:
    print(drink[0] + drink[1])

else:
    dp = [0] * n
    dp[0] = drink[0]
    dp[1] = drink[0] + drink[1]
    dp[2] = max(drink[0] + drink[2], drink[1] + drink[2], dp[1])

    for i in range(3, n):
        dp[i] = max(dp[i-1],
                    dp[i-2] + drink[i],
                    dp[i-3] + drink[i-1] + drink[i])

    print(dp[-1])