# programmers: H-Index

def solution(citations):
    citations.sort(reverse=True)

    for i in range(len(citations)):
        if citations[i] < i + 1:
            return i

    return len(citations)  # 리스트 내용이 모두 동일할 경우