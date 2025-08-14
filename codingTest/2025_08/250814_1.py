# programmers: 구명보트

def solution(people, limit):
    people.sort()
    i, j = 0, len(people) - 1
    boat = 0

    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1

        j -= 1
        boat += 1

    return boat