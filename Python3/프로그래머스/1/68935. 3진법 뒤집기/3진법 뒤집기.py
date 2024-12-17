def solution(n):
    answer = 0
    strr = ''
    while n!=0: 
        strr += str(n%3)
        n = n//3
    return int(strr,3)