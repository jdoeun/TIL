# programmers: 여행경로 dfs
# dfs를 써야할 것 같은 느낌적 느낌
# 어렵다 .. 스택에서 더 이상 갈 곳이 없을 때마다 path에 추가.

def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True) # 알파벳 순서의 역순으로

    stack = ["ICN"] # 어차피 무조건 시작은 인천 공항
    path = []

    while stack:
        top = stack[-1]

        # 어떤 공항에서 출발하는 표가 없거나 표는 있었는데 없게 된다면
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]

    return path[::-1] # 역순으로 출력

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))