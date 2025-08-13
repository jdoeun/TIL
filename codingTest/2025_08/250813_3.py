# programmers: 큰 수 만들기

from itertools import combinations

def solution(number, k):
    num_list = []

    for i in range(len(number)):
        num_list.append(number[i])

    answer_list = list(set(combinations(num_list, len(number) - k)))

    result = []

    for tup in answer_list:
        num = ''
        for t in tup:
            num += t

        result.append(num)

    return max(result)