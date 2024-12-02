class Person:

    def __init__(self, name: str, age:int, gender: str):
        self.name:str = name
        self.age:int = age

        while gender not in ["male", "female"]:
            print("*****male 또는 female만 입력 가능*****")
            gender = input("성별 재입력: ").lower()
        self.gender:str = gender

    def __repr__(self):
        return f"이름: {self.name}, 성별: {self.gender}\n나이: {self.age}"

    def greet(self):
        if self.age > 19:
            print("너 성인임?")
        else:
            print("너 미성년자임?")

name = input("이름: ")
age = int(input("나이: "))
gender = input("성별 (male/female): ").lower()

person = Person(name, age, gender)
display(person) # 주피터 노트북 사용
person.greet()
