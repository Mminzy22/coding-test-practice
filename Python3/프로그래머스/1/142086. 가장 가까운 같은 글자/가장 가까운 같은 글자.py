def solution(s):
    idx = {}
    answer = []
    for i, c in enumerate(s):
        if c in idx:
            answer.append(i - idx[c])
        else:
            answer.append(-1)
        idx[c] = i
    return answer

