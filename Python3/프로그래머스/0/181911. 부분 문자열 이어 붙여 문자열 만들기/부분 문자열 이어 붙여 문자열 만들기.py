def solution(my_strings, parts):
    answer = ''
    for i, x in enumerate(parts):
        answer += my_strings[i][x[0]:x[1]+1]
    return answer