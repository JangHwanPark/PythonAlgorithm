class Bank:
    def __init__(self, data):
        self.data = data

    def getInterestRate(self, data):
        return data.data


class BadBank(Bank):
    pass


class NormalBank(Bank):
    pass


class GoodBank(Bank):
    pass


bad_bank = BadBank(10.0)
print('BadBank의 이자율:', bad_bank.getInterestRate(bad_bank))

normal_bank = NormalBank(5.0)
print('NormalBank의 이자율:', normal_bank.getInterestRate(normal_bank))

good_bank = GoodBank(3.0)
print('GoodBank의 이자율:', good_bank.getInterestRate(good_bank))
