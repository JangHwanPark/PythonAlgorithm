class Employee:
    def __init__ (self, name, price):
        self.name = name
        self.price = price
        #self.plus =plus

    def getSalary(self):
        print('이름:', self.name, '; 월급:' ,self.price) #, '; 보너스:', self.plus


class Manager(Employee):
    def __init__(self, plus, name, price):
        super().__init__(name, price)
        self.plus = plus

    def getSalary(self):
        print('이름:', self.name, '; 월급:' ,self.price, '; 보너스:', self.plus) #


em = Employee("김철수", 20)
em.getSalary()

em2 = Manager('김철수', 2000000, 1000000)
em2.getSalary()