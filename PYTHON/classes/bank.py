import time
from datetime import datetime,date
import time
from datetime import datetime, date

def logger(func_type):
    def decorator(func):
        def wrapper(self, amount, *args, **kwargs):  # amount is always the 2nd arg
            start = time.time()
            result = func(self, amount, *args, **kwargs)
            end = time.time()
            
            duration = round((end - start) * 1000, 2)
            timestamp = datetime.now().isoformat()
            today = date.today()
            
            with open(f"{today}.txt", "a") as f:
                f.write(
                    f"{timestamp} : function: {func_type} : "
                    f"Amount: {amount}KES\n"
                )
            return result  # important!
        return wrapper
    return decorator
class Bank:
    bank_name="Equity Bank"
    clients=0
    def __init__(self, name, no, amount):
        self.name = name
        self.no = no
        self._cash = amount
        self._log=[]
        Bank.clients+=1 
    @property
    def cash(self):  
        return self._cash
    @logger(func_type="deposit")
    @cash.setter
    def cash(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        
        self._cash = amount
        self._log.append()
    @logger(func_type="deposit")
    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._cash += amount         
    @logger(func_type="withdrawal")
    def withdraw(self, amount):      
        if amount > self._cash:
            raise ValueError("Insufficient funds")
        self._cash -= amount

    def show_balance(self, no=None):
        if no is not None and self.no != no:
            raise PermissionError("Account number does not match")
        return self._cash

    def show_details(self, no=None):
        if no is not None and self.no != no:
            raise PermissionError("Account number does not match")
        print(f"Name: {self.name}")
        print(f"Balance: {self._cash}")
        print(f"Account No: {self.no}")
test=Bank("Tedd",1,20)
print(Bank.bank_name)
