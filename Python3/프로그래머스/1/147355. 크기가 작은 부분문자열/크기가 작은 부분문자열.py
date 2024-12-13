def solution(t, p):
    answer = 0
    for i in range(len(t)):
        if len(t[i:len(p)+i]) == len(p) and p >= t[i:len(p)+i]:
            answer +=1
    return answer