def solution(arr, k):
    result = []
    for num in arr:
        if num not in result:
            result.append(num)
        if len(result) == k:
            break
    return result + [-1] * (k - len(result))