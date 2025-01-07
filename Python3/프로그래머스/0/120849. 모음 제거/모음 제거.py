def solution(my_string):
    ab = ['a', 'e', 'i', 'o', 'u']
    answer = ''
    for c in my_string:
        if c not in ab:
            answer += c
    return answer