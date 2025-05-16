def solution(spell, dic):
    s = set(spell)
    for word in dic:
        if set(word) == s and len(word) == len(spell):
            return 1
    return 2