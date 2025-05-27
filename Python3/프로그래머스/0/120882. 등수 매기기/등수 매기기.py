def solution(score):
    avg = [(a + b) / 2 for a, b in score]
    sorted_avg = sorted(avg, reverse=True)
    return [sorted_avg.index(a) + 1 for a in avg]