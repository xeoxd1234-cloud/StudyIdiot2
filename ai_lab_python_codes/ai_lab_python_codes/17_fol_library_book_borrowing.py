"""FOL-style inference — Rahul's library book borrowing eligibility."""

facts = {
    "Member(Rahul)",
    "ValidID(Rahul)",
    "NoFines(Rahul)",
}

if "Member(Rahul)" in facts and "ValidID(Rahul)" in facts:
    facts.add("LibraryAccess(Rahul)")

if "LibraryAccess(Rahul)" in facts and "NoFines(Rahul)" in facts:
    facts.add("CanBorrow(Rahul)")

if __name__ == "__main__":
    print("Can borrow book:", "CanBorrow(Rahul)" in facts)
