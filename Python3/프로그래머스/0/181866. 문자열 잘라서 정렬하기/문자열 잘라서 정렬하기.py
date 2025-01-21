def solution(myString):
    strs = myString.split('x')
    answer = [s for s in strs if s]
    return sorted(answer)