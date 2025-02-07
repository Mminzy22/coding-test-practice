def solution(box, n):
    t, l, h = box[0]//n, box[1]//n, box[2]//n
    return t*l*h