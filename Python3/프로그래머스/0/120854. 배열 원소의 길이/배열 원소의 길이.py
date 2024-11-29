def solution(strlist):
    answer = []
    for i in range(len(strlist)):
        answer.insert(i, len(strlist[i]))
    return answer