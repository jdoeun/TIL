# programmers: 가장 큰 수

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True) # 각 숫자가 1000 이하이므로
    return str(int(''.join(numbers)))