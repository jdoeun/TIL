# programmers: 메뉴 리뉴얼

from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for c in course:
        combination_counts = Counter()

        # 조합 개수 세기
        for order in orders:
            order_combinations = combinations(sorted(order), c)
            combination_counts.update(order_combinations)

        if combination_counts:
            max_count = max(combination_counts.values(), default=0)

            if max_count >= 2:
                for key, value in combination_counts.items():
                    if value == max_count:
                        answer.append("".join(key))

    return sorted(answer)