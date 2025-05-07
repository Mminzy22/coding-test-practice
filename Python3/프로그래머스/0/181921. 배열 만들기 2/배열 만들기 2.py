def solution(l, r):
    answer = []
    for num in range(l, r+ 1):
        if all(ch in '05' for ch in str(num)):
            answer.append(num)
    return answer if answer else [-1]