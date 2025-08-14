# programmers: H-Index

def solution(citations):
    answer = []
    max_citation = len(citations)

    for i in range(max_citation, 0, -1):
        max_count = 0
        for c in citations:
            if c >= i:
                max_count += 1

        if max_count >= i:
            answer.append(i)

    return max(answer) if answer else 0