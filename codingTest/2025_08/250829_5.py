# programmers : N개의 최소공배수

import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)


def solution(arr):
    n = arr[0]

    for i in arr[1:]:
        n = lcm(n, i)
    return n