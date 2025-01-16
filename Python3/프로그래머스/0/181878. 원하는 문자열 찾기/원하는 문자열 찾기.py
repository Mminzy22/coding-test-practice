def solution(myString, pat):
    answer = 1 if str.upper(pat) in str.upper(myString) else 0
    return answer