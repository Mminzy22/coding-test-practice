def solution(arr, queries):
    n = len(arr)
    diff = [0] * (n + 1)

    for s, e in queries:
        diff[s] += 1
        if e + 1 < n:
            diff[e + 1] -= 1

    for i in range(n):
        if i > 0:
            diff[i] += diff[i - 1]
        arr[i] += diff[i]

    return arr