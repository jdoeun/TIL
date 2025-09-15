# BOJ: 14501 퇴사 재귀

N = int(input())
timeTable = [list(map(int, input().split())) for _ in range(N)]

def solve(i):
    if i>=N: # 0일부터 n-1일까지만 상담 가능
        return 0
    ret = 0
    if i + timeTable[i][0] <= N:
        ret = solve(i+timeTable[i][0]) + timeTable[i][1]
    ret = max(ret, solve(i+1))
    return ret

print(solve(0))