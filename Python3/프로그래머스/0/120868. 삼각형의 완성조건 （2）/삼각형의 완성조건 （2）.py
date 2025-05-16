def solution(sides):
    return (sum(sides) - 1) - abs(sides[0] - sides[1])