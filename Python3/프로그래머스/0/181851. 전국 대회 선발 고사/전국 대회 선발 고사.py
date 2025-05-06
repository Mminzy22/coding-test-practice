def solution(rank, attendance):
    students = [(r, i) for i, r in enumerate(rank)]
    students.sort()
    selected = []
    for r, i in students:
        if attendance[i]:
            selected.append(i)
        if len(selected) == 3:
            break
    a, b, c = selected
    return 10000 * a + 100 * b + c