def solution(arr):
    return [
        c // 2 if c >= 50 and c % 2 == 0 else 
        c * 2 if c < 50 and c % 2 != 0 else 
        c 
        for c in arr
    ]