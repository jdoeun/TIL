# programmers: 큰 수 만들기

# 스택 이용한 greedy 풀이
def solution1(number, k):
    answer = []

    for n in number:
        # while문을 써서 스택 안에 있는 모든 n보다 작은 숫자 확인
        while k > 0 and answer and answer[-1] < n:
            answer.pop()
            k -= 1

        answer.append(n)

    # 그냥 스택을 합쳤을 때 만약 answer이 내림차순인 경우 고려해야함
    return ''.join(answer[:len(answer) - k])


# 완전탐색 풀이 -> 몇개 테케에서 시간 초과 ㅜㅜ
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