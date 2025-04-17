def solution(my_string):
    count = [0] * 52
    
    for char in my_string:
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')
        elif 'a' <= char <= 'z':
            index = ord(char) - ord('a') + 26
        else:
            continue
        count[index] += 1
    
    return count