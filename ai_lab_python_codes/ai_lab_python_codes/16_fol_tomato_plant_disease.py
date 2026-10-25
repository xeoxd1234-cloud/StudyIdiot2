"""FOL-style inference — determine whether a tomato plant is diseased."""

facts = {
    "YellowLeaves(Tomato)",
    "BrownSpots(Tomato)",
    "InGarden(Tomato)",
}

if "YellowLeaves(Tomato)" in facts:
    facts.add("NutrientDeficiency(Tomato)")

if "BrownSpots(Tomato)" in facts:
    facts.add("Disease(Tomato)")

if __name__ == "__main__":
    print("Disease detected:", "Disease(Tomato)" in facts)
