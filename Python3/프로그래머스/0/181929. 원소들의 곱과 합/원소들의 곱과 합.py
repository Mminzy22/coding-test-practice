def solution(num_list):
    n = num_list[0]
    for num in num_list[1:]:
        n *= num
    m = sum(num_list)**2
    return 1 if n < m else 0