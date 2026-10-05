"""
Problem: Python Variables and Dynamic Typing
Author: Bhavishya Dewangan
"""

def demonstrate_types():
    student_name: str = "Bhavishya Dewangan"
    semester: int = 3
    cgpa: float = 8.85
    is_enrolled: bool = True
    skills: list = ["C++", "Python", "DSA", "Web Dev"]

    print(f"Student: {student_name} (Sem {semester})")
    print(f"CGPA: {cgpa} | Enrolled: {is_enrolled}")
    print(f"Core Competencies: {', '.join(skills)}")

if __name__ == "__main__":
    demonstrate_types()
