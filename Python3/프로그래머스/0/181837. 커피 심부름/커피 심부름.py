def solution(order):
    total = 0
    for item in order:
        if 'americano' in item or item == 'anything':
            total += 4500
        else:
            total += 5000
    return total