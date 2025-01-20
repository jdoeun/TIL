# programmers: 폰켓몬

def solution(nums):
    list = []

    for i in range(len(nums)):
        if nums[i] not in list:
            list.append(nums[i])

    if len(list) >= (len(nums) / 2):
        answer = len(nums) / 2

    else:
        answer = len(list)

    return answer

print(solution([3,3,3,2,2,2]))