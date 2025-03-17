# programmers: 튜플

def solution(s):
    li = []
    for i in s.split("},"):  # 문자열 대체, 분리
        li.append(i.replace("{", "").replace("}", "").split(","))
    li.sort(key=len)  # 길이 순으로 정렬

    answer = []

    for i in li:
        for j in i:
            if not j in answer:
                answer.append(j)

    return list(map(int, answer))