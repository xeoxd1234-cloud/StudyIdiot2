"""FOL-style inference — Amit's promotion eligibility."""

facts = {
    "Employee(Amit)",
    "FiveYearsService(Amit)",
    "GoodPerformance(Amit)",
}

if "FiveYearsService(Amit)" in facts:
    facts.add("Experienced(Amit)")

if "Experienced(Amit)" in facts and "GoodPerformance(Amit)" in facts:
    facts.add("PromotionEligible(Amit)")

if __name__ == "__main__":
    print("Promotion eligible:", "PromotionEligible(Amit)" in facts)
