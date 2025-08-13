# programmers: 여행경로

def solution(tickets):
    # 딕셔너리로 각 출발점에서 갈 수 있는 공항들을 value에 저장
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)  # pop 할 때 알파벳 순서 앞서는거 먼저 넣어야 하므로

    stack = ["ICN"]
    answer = []

    while stack:
        top = stack[-1]

        if top in routes and routes[top]:
            stack.append(routes[top].pop())

        else:
            answer.append(stack.pop())

    return answer[::-1]