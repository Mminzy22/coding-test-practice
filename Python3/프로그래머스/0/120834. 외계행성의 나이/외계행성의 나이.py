def solution(age):
    a = {str(i): chr(97 + i) for i in range(10)}
    return ''.join(a[ag] for ag in str(age))