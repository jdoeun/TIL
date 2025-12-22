# BOJ: 2446 별 찍기 - 9

n = int(input())

for i in range(n, 0, -1):
    print(" " * (n-i) + "*" * i + "*" * (i-1))

for i in range(2, n+1):
    print(" " * (n-i) + "*" * i + "*" * (i-1))