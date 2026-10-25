"""Route Planning — Depth-First Search (DFS)."""

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": ["E"],
    "E": [],
}


def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    path.append(start)
    visited.add(start)
    if start == goal:
        return path.copy()

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, visited, path)
            if result:
                return result

    path.pop()
    return None


if __name__ == "__main__":
    print("DFS Path:", dfs(graph, "A", "E"))
