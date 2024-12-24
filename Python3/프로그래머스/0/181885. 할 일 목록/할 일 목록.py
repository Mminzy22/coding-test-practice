def solution(todo_list, finished):
    answer = []
    for i,to in enumerate(todo_list):
        if not finished[i]:
            answer.append(to)
    return answer