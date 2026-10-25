"""FOL-style inference — classify Tommy as a mammal and animal."""

facts = {"Dog(Tommy)", "FourLegs(Tommy)", "Pet(Tommy)"}

if "Dog(Tommy)" in facts:
    facts.add("Mammal(Tommy)")

if "Mammal(Tommy)" in facts:
    facts.add("Animal(Tommy)")

if __name__ == "__main__":
    print("Is Tommy an animal:", "Animal(Tommy)" in facts)
