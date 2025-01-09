def solution(n):
    answer = 0  # 자릿수 합을 저장할 변수 초기화
    
    # 8자리부터 1자리까지 반복 (큰 자릿수부터 계산)
    for i in range(8, 0, -1):
        
        # 10^i (10의 거듭제곱)으로 나눈 나머지가 n이면 해당 자릿수는 0
        if n % pow(10, i) == n:
            continue  # 다음 자릿수로 넘어감
        
        else:
            # n을 10^i로 나눈 몫 (현재 자릿수의 값)
            num = n // pow(10, i)
            
            # 현재 자릿수를 answer에 더함
            answer += num
            
            # 자릿수를 제외하고 남은 숫자를 계산
            n = n - num * pow(10, i)
    
    # 마지막 1의 자릿수 처리
    answer += n

    return answer  # 자릿수 합 반환

# # 코드 개선
# def solution(n):
#     return sum(int(i) for i in str(n))