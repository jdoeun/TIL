# programmers: 할인 행사

from collections import Counter

def solution(want, number, discount):
    answer = 0
    # zip 하면 튜플로 반환 -> 딕셔너리로 만듦
    want_counter = Counter(dict(zip(want, number)))

    for start in range(len(discount) - 9):
        discount_counter = Counter(discount[start:start + 10])

        if all(discount_counter[item] >= want_counter[item] for item in want):
            answer += 1

    return answer