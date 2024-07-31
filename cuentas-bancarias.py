class Bankaccount:
    def __init__(self, accountholder, balance):
        self.accountholder= accountholder
        self.balance= balance
        self.isactive= True

    def deposit(self, amount):
        if self.isactive:
            self.balance += amount
            print(f"se ha depositado {amount}. saldo actual {self.balance}")
        else:
            print("cuenta inactiva")
    def withraw(self, amount):
        if self.active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"saldo actual: {self.balance}")
    
    def desactivate(self):
        self.isactive= False
        print(f"la cuenta ha sido desactivada")

    def activate(self):
        self.isactive= True
        print(f"la cuenta ha sido activada")

account1=Bankaccount("ana", 500)
account2=Bankaccount("juan", 700)
account3=Bankaccount("pedro", 600)

#llamada alos metodos

account1.deposit(200)
account2.deposit(100)
account3.desactivate()
account2.deposit(300)
account1.desactivate()
account1.deposit(20)