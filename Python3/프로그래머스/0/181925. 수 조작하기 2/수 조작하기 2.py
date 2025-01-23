def solution(numLog):
    return ''.join(
        "w" if diff == 1 else
        "s" if diff == -1 else
        "d" if diff == 10 else
        "a"
        for diff in (b - a for a, b in zip(numLog, numLog[1:]))
    )