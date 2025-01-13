def solution(keyinput, board):
    answer = [0, 0]
    tw = board[0] // 2
    th = board[1] // 2
    whs = {
        "up": [0, 1],
        "down": [0, -1],
        "left": [-1, 0],
        "right": [1, 0]
    }
    for key in keyinput:
        w, h = whs[key]
        answer[0] += w
        answer[1] += h
        answer[0] = max(-tw, min(tw, answer[0]))
        answer[1] = max(-th, min(th, answer[1]))
    return answer