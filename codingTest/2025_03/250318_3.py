# programmers: 귤 고르기

from collections import Counter


def solution(k, tangerine):
    counts = Counter(tangerine)
    sorted_counts = sorted(counts.values(), reverse=True)

    total = 0
    answer = 0

    for count in sorted_counts:
        total += count
        answer += 1

        if total >= k:
            break

    return answer