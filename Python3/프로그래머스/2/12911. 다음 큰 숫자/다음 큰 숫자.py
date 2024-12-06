def solution(n):
    b = n+1
    while bin(n).count('1') != bin(b).count('1'):
        b += 1
    return b