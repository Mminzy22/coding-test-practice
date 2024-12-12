def solution(s):
    count, zeros = 0, 0
    while '1' != s:
        zeros += s.count('0')
        s = s.replace('0','')
        s = (bin(len(s)))[2:]
        count += 1
        
    answer = [count,zeros]
    return answer