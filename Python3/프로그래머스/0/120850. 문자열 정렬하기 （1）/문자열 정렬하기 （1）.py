def solution(my_string):
    answer = [int(d) for d in my_string if d.isdigit()]
    return sorted(answer)