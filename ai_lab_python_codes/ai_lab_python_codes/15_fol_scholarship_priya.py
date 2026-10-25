"""FOL-style inference — Priya's scholarship eligibility."""

facts = {
    "Student(Priya)",
    "GoodAttendance(Priya)",
    "GoodMarks(Priya)",
}

if "GoodAttendance(Priya)" in facts:
    facts.add("ExamEligible(Priya)")

if "ExamEligible(Priya)" in facts and "GoodMarks(Priya)" in facts:
    facts.add("Scholarship(Priya)")

if __name__ == "__main__":
    print("Scholarship eligible:", "Scholarship(Priya)" in facts)
