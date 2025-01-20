def solution(my_strings, parts):
    answer = ''
    for i, (x,y) in enumerate(parts):
        answer += my_strings[i][x:y+1]
    return answer