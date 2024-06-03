class Person:
    # 생성자
    def __init__(self):
        self.name = 'name'
        self.age = 25


class ExtendsPerson(Person):
    pass


p1 = Person()
print(p1.name, p1.age)

ep = ExtendsPerson()
print(ep.name, ep.age)