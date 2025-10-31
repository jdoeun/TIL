# BOJ: 11055 가장 큰 증가하는 부분 수열

n = int(input())
A = list(map(int, input().split()))

dp = [0] * n
dp[0] = A[0]

for i in range(n):
    dp[i] = A[i]
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], A[i] + dp[j])

print(max(dp))