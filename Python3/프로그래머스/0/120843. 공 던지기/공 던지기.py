def solution(numbers, k):
    index = 0
    for _ in range(k - 1):
        index = (index + 2) % len(numbers)
    return numbers[index]