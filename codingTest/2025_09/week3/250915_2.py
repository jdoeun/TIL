# BOJ: 14888 연산자 끼워넣기 백트래킹(dfs)

import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split())) # +, -, *, //

maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum

    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    # if문을 여러개 타고 들어가면서 현재 함수로 돌아와 같은 depth에서 다른 선택지를 시도 가능
    # 백트래킹
    if plus:
        dfs(depth+1, total+num[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total-num[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, total*num[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(total / num[depth]), plus, minus, multiply, divide-1)

dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)

