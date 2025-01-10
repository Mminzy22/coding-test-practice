def solution(numbers):
    answer = set()
    for i, n in enumerate(numbers):
        for j, num in enumerate(numbers):
            if i != j:
                answer.add(n + num)
    return sorted(answer)