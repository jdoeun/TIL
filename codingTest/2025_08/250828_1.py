# programmers : 이진 변환 반복하기

def solution(s):
    answer = []
    cnt = 0
    zeroCnt = 0

    while True:
        if s == "1":
            break

        zeroCnt += s.count("0")
        s = s.replace("0", '')  # 다시 s에 저장해 주어야 함
        s = bin(len(s))[2:]

        cnt += 1

    answer = [cnt, zeroCnt]
    return answer