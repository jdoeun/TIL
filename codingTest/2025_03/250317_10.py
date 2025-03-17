# programmers: 카펫

def solution(brown, yellow):
    gop = brown + yellow

    for width in range(1, gop + 1):
        if gop % width == 0:
            height = gop // width

            if (width - 2) * (height - 2) == yellow:
                return sorted([width, height], reverse=True)