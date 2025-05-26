def solution(chicken):
    s = 0
    while chicken >= 10:
        new_s = chicken // 10
        s += new_s
        chicken = new_s + (chicken % 10)
    return s