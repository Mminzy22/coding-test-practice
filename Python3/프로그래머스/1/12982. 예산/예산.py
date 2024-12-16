def solution(d, budget):
    answer = 0
    for i in sorted(d):
        budget -= i
        print(budget)
        if budget < 0 :
            continue
        else:
            answer+=1
    return answer