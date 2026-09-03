class Bank:
    def __init__(self, name, no, amount):
        self.name = name
        self.no = no
        self._cash = amount 
    @property
    def cash(self):  
        return self._cash

    @cash.setter
    def cash(self, amount):          # SETTER
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._cash = amount

    def deposit(self, amount):       # method to add money
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._cash += amount         # uses the internal variable directly

    def withdraw(self, amount):      # method to subtract (with check)
        if amount > self._cash:
            raise ValueError("Insufficient funds")
        self._cash -= amount

    def show_balance(self, no=None): # optional account number check
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
test.deposit(400)
test.show_details()