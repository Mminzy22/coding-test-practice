def solution(n):
    return sum(1 for i in range(1, n + 1) if sum(i % j == 0 for j in range(1, i + 1)) >= 3)