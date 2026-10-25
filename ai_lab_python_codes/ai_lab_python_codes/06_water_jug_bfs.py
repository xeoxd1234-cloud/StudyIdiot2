"""Water Jug Problem — Breadth-First Search."""

from collections import deque


def water_jug_bfs(capacity_a, capacity_b, target):
    start = (0, 0)
    queue = deque([start])
    visited = {start}

    while queue:
        x, y = queue.popleft()
        if x == target or y == target:
            return True

        states = [
            (capacity_a, y),  # Fill A
            (x, capacity_b),  # Fill B
            (0, y),           # Empty A
            (x, 0),           # Empty B
            (min(x + y, capacity_a), max(0, x + y - capacity_a)),
            (max(0, x + y - capacity_b), min(x + y, capacity_b)),
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
    return False


if __name__ == "__main__":
    print("Possible:", water_jug_bfs(4, 3, 2))
