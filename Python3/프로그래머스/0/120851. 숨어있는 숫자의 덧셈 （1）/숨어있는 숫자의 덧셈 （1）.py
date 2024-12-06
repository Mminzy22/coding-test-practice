def solution(my_string):
    num = 0
    
    for char in my_string:
        if char.isdigit():
            num += int(char)
            
    return num