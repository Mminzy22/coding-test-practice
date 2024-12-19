def solution(s):
    a =[]
    for c in s:
        if a and a[-1] == c:
            a.pop()
        else:
            a.append(c)
    return 1 if not a else 0