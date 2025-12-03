# BOJ: 11720 숫자의 합

N = int(input())
num = input()

sum = 0
for i in range(N):
    sum += int(num[i])

print(sum)