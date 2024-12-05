def solution(money):
    # 아이스 아메리카노의 가격
    price = 5500
    
    # 잔 수와 남는 돈 계산
    cups = money // price  # 최대 잔 수
    remaining = money % price  # 남는 돈
    
    return [cups, remaining]