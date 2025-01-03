def solution(sizes):
    w = [(max(w, h), min(w, h)) for w, h in sizes]
    
    mw= max(size[0] for size in w)
    mh = max(size[1] for size in w)
    
    return mw * mh