def solution(arr, queries):
    answer = []
    for a in queries:
        b = arr[a[0]:a[1]+1]
        filtered = [num for num in b if num > a[2]]
        if filtered:
            answer.append(min(filtered))
        else:
            answer.append(-1)
    return answer