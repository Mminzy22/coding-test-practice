import random

while True:
    print("1. 게임시작")
    print("2. 종료")
    choice = input("번호를 선택하셔유 > ")

    if choice == "1":
        com = random.randint(1, 10)
        print("컴퓨터가 1과 10 사이의 숫자 랜덤으로 정했음. 숫자 맞추셈")

        while True:
            try:
                pl_num = int(input("예상 숫자 적으셈: "))
                if 0< pl_num < 11:
                    if pl_num > com:
                        print("너가 적은 숫자가 더 큼.")
                    elif pl_num < com:
                        print("너가 적은 숫자가 더 작음")
                    else:
                        print("****************정답임****************")
                        break
                else:
                    print("1과 10 사이의 숫자를 적으셈")
            except ValueError:
                print("숫자만 입력해야됨. 다시 입력하셈")
    elif choice == "2":
        print("게임 종료합니다")
        break
    else:
        print("제대로 된 번호 입력 하셈")
