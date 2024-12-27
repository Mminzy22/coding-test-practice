def solution(num_list):
    for i, num in enumerate(num_list):
        if num<0:
            answer = i
            break
        elif num_list.count(-1)==0:
            answer = -1
    return answer