from collections import Counter

def solution(strArr):
    lengths = [len(s) for s in strArr]
    count_by_length = Counter(lengths)
    return max(count_by_length.values())
