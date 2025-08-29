# 프로그래머스 - 귤 고르기

from collections import Counter

def solution(k, tangerine):
    answer = 0

    tangerine_dict = Counter(tangerine)
    tangerine_list = sorted(tangerine_dict.values(), reverse=True)

    # 많은 거부터 빼면 크기 종류가 최소가 됨
    for t in tangerine_list:
        k -= t
        answer += 1

        if k <= 0:
            break

    return answer