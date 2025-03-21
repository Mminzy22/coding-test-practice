def solution(myString, pat):
    last_index = myString.rfind(pat)
    return myString[:last_index + len(pat)]