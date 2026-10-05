"""
Problem: Custom Exceptions and Defensive Programming
Author: Bhavishya Dewangan
"""

class InsufficientFundsError(Exception):
    def __init__(self, requested: float, available: float):
        super().__init__(f"Requested ₹{requested:.2f} exceeds available balance ₹{available:.2f}")
        self.requested = requested
        self.available = available

def process_payment(balance: float, cost: float) -> float:
    if cost > balance:
        raise InsufficientFundsError(cost, balance)
    return balance - cost

if __name__ == "__main__":
    current = 2500.0
    for purchase in [1200.0, 3000.0]:
        try:
            print(f"Attempting purchase of ₹{purchase}...")
            current = process_payment(current, purchase)
            print(f"Payment approved! Remaining: ₹{current}")
        except InsufficientFundsError as err:
            print(f"[ERROR CAUGHT] {err}")
        finally:
            print("Transaction cycle complete.\n")
