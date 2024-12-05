def solution(hp):
    # 병력의 공격력
    general = 5  # 장군개미
    soldier = 3  # 병정개미
    worker = 1   # 일개미

    # 장군개미로 처리할 수 있는 수 계산
    generals = hp // general
    remaining_hp = hp % general

    # 병정개미로 처리할 수 있는 수 계산
    soldiers = remaining_hp // soldier
    remaining_hp = remaining_hp % soldier

    # 일개미로 처리할 수 있는 수 계산
    workers = remaining_hp // worker

    # 총 병력 수
    return generals + soldiers + workers