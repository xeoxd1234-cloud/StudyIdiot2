"""Route Planning — Iterative Deepening Search (IDS)."""

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": ["E"],
    "E": [],
}


def depth_limited_search(node, goal, limit, path):
    path.append(node)
    if node == goal:
        return path.copy()

    if limit > 0:
        for neighbor in graph[node]:
            result = depth_limited_search(neighbor, goal, limit - 1, path)
            if result:
                return result

    path.pop()
    return None


def ids(start, goal, max_depth):
    for depth in range(max_depth + 1):
        result = depth_limited_search(start, goal, depth, [])
        if result:
            return result
    return None


if __name__ == "__main__":
    print("IDS Path:", ids("A", "E", 4))
