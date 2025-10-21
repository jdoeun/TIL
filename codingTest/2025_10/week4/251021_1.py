# BOJ: 1463 1로 만들기

n = int(input())

# DP 테이블 초기화
d = [0] * 1000001

# Bottom-Up 방식
for i in range(2, n+1):
    d[i] = d[i-1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

print(d[n])