import re
def solution(myStr):
    split_str = re.split('[abc]', myStr)
    result = [s for s in split_str if s]
    return result if result else ["EMPTY"]