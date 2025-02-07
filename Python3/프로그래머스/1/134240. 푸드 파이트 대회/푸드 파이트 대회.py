def solution(food):
    left_side = "".join(str(i) * (food[i] // 2) for i in range(1, len(food)))
    return left_side + "0" + left_side[::-1]