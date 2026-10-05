"""
Problem: List and Dictionary Comprehensions
Author: Bhavishya Dewangan
"""

def main():
    # List comprehension: squares of even numbers up to 20
    even_squares = [x**2 for x in range(1, 21) if x % 2 == 0]
    print(f"Even Squares: {even_squares}")

    # Dict comprehension: character frequency count
    sample_text = "computer science engineering"
    char_counts = {char: sample_text.count(char) for char in set(sample_text) if char != " "}
    print("Character Frequencies:")
    for k, v in sorted(char_counts.items()):
        print(f"  '{k}': {v}")

if __name__ == "__main__":
    main()
