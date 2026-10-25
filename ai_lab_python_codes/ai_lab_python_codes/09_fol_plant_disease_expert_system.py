"""Forward-chaining FOL-style inference — Plant Disease Expert System."""

facts = {"yellow_leaves", "spots", "wilting"}
rules = [
    ({"yellow_leaves", "spots"}, "fungal_infection"),
    ({"wilting", "fungal_infection"}, "plant_disease"),
    ({"yellow_leaves"}, "nutrient_deficiency"),
]


def infer(initial_facts, inference_rules):
    known_facts = set(initial_facts)
    changed = True

    while changed:
        changed = False
        for conditions, conclusion in inference_rules:
            if conditions <= known_facts and conclusion not in known_facts:
                known_facts.add(conclusion)
                changed = True
    return known_facts


if __name__ == "__main__":
    print(infer(facts, rules))
