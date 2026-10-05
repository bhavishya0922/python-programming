"""
Problem: Python OOP with Property Decorators & Magic Methods
Author: Bhavishya Dewangan
"""

class Account:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self._balance = max(0.0, initial_balance)

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def __repr__(self) -> str:
        return f"Account(owner='{self.owner}', balance={self._balance:.2f})"

if __name__ == "__main__":
    acc = Account("Bhavishya Dewangan", 5000.0)
    print(acc)
    acc.deposit(2000.0)
    acc.withdraw(1500.0)
    print(f"Final Balance: ₹{acc.balance:.2f}")
