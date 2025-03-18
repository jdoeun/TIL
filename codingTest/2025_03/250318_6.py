# programmers: 영어 끝말잇기

def solution(n, words):
    used_words = set()  # 중복 체크용 set
    used_words.add(words[0])  # 첫 번째 단어 미리 추가

    for i in range(1, len(words)):
        # 중복 단어 OR 끝말잇기 규칙 위반 검사
        if words[i] in used_words or words[i][0] != words[i - 1][-1]:
            return [(i % n) + 1, (i // n) + 1]  # [몇 번째 사람, 몇 번째 차례]

        used_words.add(words[i])  # 단어 추가

    return [0, 0]  # 정상적으로 끝말잇기 완료된 경우