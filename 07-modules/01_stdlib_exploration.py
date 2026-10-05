"""
Problem: Standard Library Utilities
Author: Bhavishya Dewangan
"""
import math
import random
from datetime import datetime

def main():
    now = datetime.now()
    print(f"Timestamp: {now.strftime('%Y-%m-%d %H:%M:%S')}")

    num = 144
    print(f"Square root of {num}: {math.isqrt(num)}")
    print(f"GCD(48, 180): {math.gcd(48, 180)}")

    dice_rolls = [random.randint(1, 6) for _ in range(5)]
    print(f"5 Random Dice Rolls: {dice_rolls}")

if __name__ == "__main__":
    main()
