def solution(rsp):
    # 이기는 경우를 매핑
    win_map = {'2': '0', '0': '5', '5': '2'}
    
    # 입력 문자열을 변환
    result = ''.join(win_map[char] for char in rsp)
    
    return result