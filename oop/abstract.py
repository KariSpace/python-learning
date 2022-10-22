from abc import ABC, abstractmethod


class ATM(ABC):

    @abstractmethod
    def __init__(self, money):
        self.blocked = False
        self.volume = 5000
        self.money = money

    # общие методы, который будут использовать все наследники этого класса
    def blockATM(self):
        self.blocked = True
        print("ATM was blocked")

    def unblockATM(self):
        self.blocked = False
        print("ATM unblocked")

    def callTheIncasator(self):
        self.money = self.volume
        self.unblockATM()

    # абстрактные методы, которые будет необходимо переопределять для каждого подкласса
    @abstractmethod
    def givemoney(self):
        pass





class Default_ATM(ATM):
        
    def __init__(self, money):
        self.blocked = False
        self.volume = 10000
        self.money = money
  
    def givemoney(self, moneyToWithdraw):
        if(not self.blocked):
            print("Success {money}".format(money=moneyToWithdraw))


# atm1 = Default_ATM(10)
# atm1.givemoney(200)
# atm1.givemoney(200)
# atm1.callTheIncasator()
# atm1.givemoney(200)