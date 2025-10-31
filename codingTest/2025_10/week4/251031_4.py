# BOJ: 11054 가장 긴 바이토닉 부분 수열

n = int(input())
A = list(map(int, input().split()))

dp = [1] * n
dp_reverse =  [1] * n

for i in range(n):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if A[i] > A[j]:
            dp_reverse[i] = max(dp_reverse[i], dp_reverse[j] + 1)

answer = 0
for i in range(n):
    answer = max(answer, dp[i] + dp_reverse[i] - 1)

print(answer)