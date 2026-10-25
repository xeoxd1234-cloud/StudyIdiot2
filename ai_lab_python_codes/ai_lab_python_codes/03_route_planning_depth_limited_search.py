"""Route Planning — Depth-Limited Search (DLS)."""

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": ["E"],
    "E": [],
}


def dls(graph, node, goal, limit, path=None):
    if path is None:
        path = []

    path.append(node)
    if node == goal:
        return path.copy()
    if limit == 0:
        path.pop()
        return None

    for neighbor in graph[node]:
        result = dls(graph, neighbor, goal, limit - 1, path)
        if result:
            return result

    path.pop()
    return None


if __name__ == "__main__":
    print("DLS Path:", dls(graph, "A", "E", 3))
