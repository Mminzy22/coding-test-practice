def solution(s):
    print(s)
    an = 0
    for i in range(len(s)):
        if s[i] == '(':
            an += 1
        else:
            an -= 1
        if an < 0:
            return False
    return an == 0
    