def solution(myString, pat):
    trans_table = str.maketrans("AB", "BA")
    transformed = myString.translate(trans_table)
    return 1 if pat in transformed else 0