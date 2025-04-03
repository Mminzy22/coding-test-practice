def solution(intStrs, k, s, l):
    answer = []
    for nums in intStrs:
        num = int(nums[s:s+l])
        if num > k:
            answer.append(num)
    return answer