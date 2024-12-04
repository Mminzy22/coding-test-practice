def solution(s):
    print(s)
    an = 0
    for c in s:
        if c == '(':
            an += 1
        else:
            an -= 1
        if an < 0:
            return False
    return an == 0
    