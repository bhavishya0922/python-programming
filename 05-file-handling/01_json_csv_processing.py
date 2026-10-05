"""
Problem: Structured JSON and CSV Handling
Author: Bhavishya Dewangan
"""
import json
import csv

def demo_file_io():
    data = [
        {"roll_no": 101, "name": "Bhavishya", "subject": "DSA", "score": 92},
        {"roll_no": 102, "name": "Aryan", "subject": "DSA", "score": 88},
        {"roll_no": 103, "name": "Priya", "subject": "DSA", "score": 95}
    ]

    # Save to JSON
    json_path = "students.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"Saved {len(data)} records to {json_path}")

    # Read back and parse
    with open(json_path, "r", encoding="utf-8") as f:
        loaded = json.load(f)
    print(f"Read back from JSON: {loaded[0]['name']} scored {loaded[0]['score']}")

if __name__ == "__main__":
    demo_file_io()
