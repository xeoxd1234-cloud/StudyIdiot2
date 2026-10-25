"""FOL-style rule inference — Rahul's scholarship eligibility."""

facts = {
    "Student(Rahul)",
    "GoodAttendance(Rahul)",
    "GoodPerformance(Rahul)",
}

if "Student(Rahul)" in facts and "GoodAttendance(Rahul)" in facts:
    facts.add("ExamEligible(Rahul)")

if "ExamEligible(Rahul)" in facts and "GoodPerformance(Rahul)" in facts:
    facts.add("ScholarshipEligible(Rahul)")

if __name__ == "__main__":
    print("Scholarship Eligible:", "ScholarshipEligible(Rahul)" in facts)
