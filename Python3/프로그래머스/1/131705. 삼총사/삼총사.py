def solution(number):
    return sum(
        1
        for i in range(len(number))
        for j in range(i + 1, len(number))
        for k in range(j + 1, len(number))
        if number[i] + number[j] + number[k] == 0
    )