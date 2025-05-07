def solution(n):
    answer = [[0] * n for _ in range(n)]
    num = 1
    le, ri = 0, n - 1
    t, b = 0, n - 1
    while le <= ri and t <= b:
        for i in range(le, ri + 1):
            answer[t][i] = num
            num += 1
        t += 1
        for i in range(t, b + 1):
            answer[i][ri] = num
            num += 1
        ri -= 1
        for i in range(ri, le - 1, -1):
            answer[b][i] = num
            num += 1
        b -= 1
        for i in range(b, t - 1, -1):
            answer[i][le] = num
            num += 1
        le += 1
    return answer