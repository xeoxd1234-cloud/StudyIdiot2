"""Simple term unification example — Student Eligibility."""


def unify(x, y, substitution=None):
    if substitution is None:
        substitution = {}

    if x == y:
        return substitution

    if isinstance(x, str) and x.islower():
        return {**substitution, x: y}
    if isinstance(y, str) and y.islower():
        return {**substitution, y: x}

    if isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):
        result = dict(substitution)
        for left, right in zip(x, y):
            result = unify(left, right, result)
            if result is None:
                return None
        return result

    return None


if __name__ == "__main__":
    print(unify(("enrolled", "X", "ai"), ("enrolled", "john", "ai")))
