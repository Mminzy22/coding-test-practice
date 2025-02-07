def solution(a, b, c):
    total = a + b + c
    squared = a**2 + b**2 + c**2
    cubed = a**3 + b**3 + c**3

    if a == b == c:  # 세 개의 값이 모두 같으면
        return total * squared * cubed
    elif a == b or b == c or a == c:  # 두 개의 값이 같으면
        return total * squared
    else:  # 모두 다르면
        return total