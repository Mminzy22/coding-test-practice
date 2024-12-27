def solution(num_list):
    a = 0
    b = 0
    for i,num in enumerate(num_list):
        if i%2==0:
            a+=num
        else:
            b+=num
    answer = a if a>b else b
    return answer