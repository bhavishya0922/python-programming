"""
Problem: Python Collections Deep Dive
Author: Bhavishya Dewangan
"""

def main():
    # Set Operations
    web_skills = {"HTML", "CSS", "JavaScript", "React"}
    systems_skills = {"C", "C++", "Linux", "Git"}
    current_learning = {"C++", "DSA", "JavaScript", "Python"}

    all_skills = web_skills | systems_skills | current_learning
    common_practical = web_skills & current_learning

    print(f"Total Unique Skill Pool ({len(all_skills)}): {all_skills}")
    print(f"Intersection (Web & Active Learning): {common_practical}")

if __name__ == "__main__":
    main()
