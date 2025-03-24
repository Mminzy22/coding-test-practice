def solution(arr, flag):
    X = []
    for i in range(len(arr)):
        if flag[i]:
            X.extend([arr[i]] * (arr[i] * 2))  # arr[i]를 arr[i] * 2번 추가
        else:
            del X[-arr[i]:]  # 마지막 arr[i]개의 원소 제거
    return X