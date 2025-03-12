# programmers: 완주하지 못한 선수

from collections import Counter

def solution(participant, completion):
    # 각 이름의 개수를 센다
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)

    # 참가자에서 완주자를 뺀 결과를 찾는다
    for person in participant_counter:
        if participant_counter[person] > completion_counter[person]:
            return person