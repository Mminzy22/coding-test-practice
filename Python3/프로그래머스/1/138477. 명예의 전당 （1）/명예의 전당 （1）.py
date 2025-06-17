def solution(k, score):
    h = []
    answer = []
    for s in score:
        h.append(s)
        h.sort(reverse=True)
        if len(h) > k:
            h.pop()
        answer.append(h[-1])
    return answer