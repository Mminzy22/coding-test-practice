def solution(s):
    n = list(map(int, s.split()))
    return " ".join(map(str, (min(n), max(n))))