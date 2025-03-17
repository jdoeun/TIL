# programmers: JadenCase 문자열 만들기

def solution(s):
    answer = ''

    li = s.lower().split(" ")
    li_2 = []

    for i in range(len(li)):
        li_2.append(li[i][:1].upper() + li[i][1:])

    return " ".join(li_2)
