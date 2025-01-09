def solution(brown, yellow):
    c = brown + yellow
    
    for h in range(1, c + 1):
        if c % h == 0:
            w = c // h
            if (w - 2) * (h - 2) == yellow:
                return [w, h]
