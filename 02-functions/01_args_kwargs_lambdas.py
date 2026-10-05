"""
Problem: Advanced Function Arguments and Lambdas
Author: Bhavishya Dewangan
"""

def compute_grade_report(student_name: str, *scores: float, **metadata) -> dict:
    if not scores:
        return {"student": student_name, "average": 0.0, "status": "No Scores"}

    average = sum(scores) / len(scores)
    status = "Pass" if average >= 40.0 else "Fail"

    report = {
        "student": student_name,
        "scores_count": len(scores),
        "average": round(average, 2),
        "status": status,
        "details": metadata
    }
    return report

if __name__ == "__main__":
    report = compute_grade_report(
        "Bhavishya",
        88.5, 92.0, 79.5, 95.0,
        department="CSE", semester=3, section="A"
    )
    print("Generated Report:", report)

    # Lambda expression: sort student tuples by marks
    students = [("Aman", 82), ("Bhavishya", 91), ("Rahul", 76)]
    students_sorted = sorted(students, key=lambda s: s[1], reverse=True)
    print("Ranked Students:", students_sorted)
