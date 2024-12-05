def solution(numbers):
    # 배열을 내림차순으로 정렬
    numbers.sort(reverse=True)
    
    # 가장 큰 두 수의 곱을 계산
    max_product = numbers[0] * numbers[1]
    
    return max_product