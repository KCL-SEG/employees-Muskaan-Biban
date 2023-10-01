"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, monthlySalary, salary, commisionType, commissionPay, hours, contractNum):
        self.name = name
        self.monthlySalary = monthlySalary
        self.salary = salary
        self.commisionType = commisionType
        self.commisionPay = commissionPay
        self.hours = hours
        self.comtractNum = contractNum

    def get_pay(self):
        if not self.commisionType:
            return self.no_commission()
        if self.commisionType == "bonus":
            return self.bonus_commission()
        if self.commisionType == "contract":
            return self.contract_commission()
            
            
    def get_contract_type(self):
        if self.monthlySalary:
            return f"monthly salary of {self.salary}"
        else:
            return f"contract of {self.hours} hours at {self.salary}/hour"
        
    def get_comission_type(self):
        if self.commisionType == 'bonus':
            return f'and receives a bonus commission of {self.commisionPay}.'
        elif self.commisionType == "contract":
            return f'and receives a commission for {self.comtractNum} contract(s) at {self.commisionPay}/contract.'

    def __str__(self):
        pay = self.get_pay()
        TempName = self.name
        contract = self.get_contract_type()
        if self.commisionType == 'bonus':
            return (f'{TempName} works on a {contract} {self.get_comission_type()} Their total pay is {pay}.')
        elif self.commisionType == "contract":
            return (f'{TempName} works on a {contract} {self.get_comission_type()} Their total pay is {pay}.')
        else:
            return (f'{TempName} works on a {contract}. Their total pay is {pay}.')
    
    def no_commission(self):
        if self.monthlySalary:
            return self.salary
        else:
            return self.hours * self.salary
        
    def bonus_commission(self):
        pay = self.no_commission()
        pay = pay + self.commisionPay
        return pay
    
    def contract_commission(self):
        pay = self.no_commission()
        pay = (pay) + (self.commisionPay * self.comtractNum)
        return pay
        
        
            
        

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', True, 4000, False, False, False, False)
print(str(billie))


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', False, 25, False, False, 100, False)
print(str(charlie))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', False, 30, "bonus", 600, 120, False)
print(str(ariel))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', True, 2000, "bonus", 1500, False, False)
print(str(robbie))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', True, 3000, "contract", 200, False, 4)
print(str(renee))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', False, 25, "contract", 220, 150, 3)
print(str(jan))
