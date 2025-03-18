# programmers: 연속 부분 수열 합의 개수

def solution(elements):
    num_set = set()

    extended = elements * 2

    for length in range(1, len(elements) + 1):
        for start in range(len(elements)):
            num_set.add(sum(extended[start:start + length]))

    return len(num_set)