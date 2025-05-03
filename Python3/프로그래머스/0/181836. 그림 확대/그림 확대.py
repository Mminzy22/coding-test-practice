def solution(picture, k):
    answer = []
    for c in picture:
        answer += [''.join(char * k for char in c)]*k
    return answer