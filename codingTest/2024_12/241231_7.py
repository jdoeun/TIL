def solution(s):
    pcount = 0
    ycount = 0

    for i in range(len(s)):
        if s[i] in ("p", "P"): # 주의하기. == ("p" or "P") 이렇게 하면 앞이랑만 비교됨
            pcount = pcount + 1
        elif s[i] in ("y", "Y"):
            ycount = ycount + 1
        else:
            continue

    if pcount == ycount:
        return True

    else:
        return False