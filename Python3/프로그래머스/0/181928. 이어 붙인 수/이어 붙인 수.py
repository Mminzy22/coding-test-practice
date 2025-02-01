def solution(num_list):
    odd_str, even_str = "", ""
    for num in num_list:
        if num % 2 == 1:
            odd_str += str(num)
        else:
            even_str += str(num)
    return int(odd_str) + int(even_str)