def solution(n):
    answer = []
    str_n = str(n)

    for i in range(len(str_n)):
        answer.append(int(str_n[i]))

    sorted_ans = sorted(answer, reverse=True)
    sorted_ans = list(map(str, sorted_ans))

    final = "".join(sorted_ans)

    return int(final)

# 더 간단한 풀이
# def solution(n):
#     ls = list(str(n))
#     ls.sort(reverse = True)
#     return int("".join(ls))