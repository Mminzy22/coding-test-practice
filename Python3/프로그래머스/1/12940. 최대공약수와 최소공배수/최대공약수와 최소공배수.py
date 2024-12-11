def solution(n, m):
    nn, mm = n, m
    while m != 0:
        n, m = m, n % m
    gcd = n

    lcm = nn * mm // gcd
    answer = [gcd, lcm]
    return answer