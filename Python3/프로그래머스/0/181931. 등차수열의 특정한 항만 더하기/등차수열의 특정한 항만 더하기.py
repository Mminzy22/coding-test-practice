def solution(a, d, included):
    answer = 0
    for idx, include in enumerate(included):
        if include:
            answer += a + d * idx
    return answer