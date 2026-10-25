"""Route Planning — Breadth-First Search (BFS)."""

from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": ["E"],
    "E": [],
}


def bfs(graph, start, goal):
    queue = deque([start])
    visited = {start}
    parent = {}

    while queue:
        node = queue.popleft()
        if node == goal:
            path = [node]
            while node in parent:
                node = parent[node]
                path.append(node)
            return path[::-1]

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)
    return None


if __name__ == "__main__":
    print("BFS Path:", bfs(graph, "A", "E"))
