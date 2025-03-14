# programmers: 의상

def solution(clothes):
    closet = {}
    for name, kind in clothes:
        if kind in closet.keys():
            closet[kind].append(name)

        else:
            closet[kind] = [name]

    answer = 1

    for _, values in closet.items():
        answer *= (len(values) + 1)

    return answer - 1