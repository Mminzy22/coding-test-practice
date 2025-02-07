def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c
        s = array[i-1:j]
        ss = sorted(s)
        answer.append(ss[k-1])
    return answer