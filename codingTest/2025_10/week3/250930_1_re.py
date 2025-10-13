# 15686 치킨 배달 복습

import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(n))
result = float('inf')
house = []
chick = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            house.append([i, j])

for chi in combinations(chick, m): # 한 조합에 대해서
    temp = 0
    for h in house: # 집들을 다 돌아야 함
        chi_len = float('inf')
        for j in range(m):
            chi_len = min(abs(chi[j][0] - h[0]) + abs(chi[j][1] - h[1]), chi_len)
        temp += chi_len
    result = min(result, temp)

print(result)