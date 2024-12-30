def solution(my_string):
    answer = sorted([my_string[-i:] for i,c in enumerate(my_string)])
    return answer