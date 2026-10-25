"""8-Puzzle Solver — A* search with Manhattan-distance heuristic."""

from heapq import heappush, heappop

START = (1, 2, 3, 4, 0, 5, 6, 7, 8)
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def neighbors(state):
    zero = state.index(0)
    row, col = divmod(zero, 3)
    result = []

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            other = nr * 3 + nc
            board = list(state)
            board[zero], board[other] = board[other], board[zero]
            result.append(tuple(board))
    return result


def heuristic(state):
    total = 0
    for index, value in enumerate(state):
        if value == 0:
            continue
        goal_index = GOAL.index(value)
        total += abs(index // 3 - goal_index // 3)
        total += abs(index % 3 - goal_index % 3)
    return total


def a_star(start=START, goal=GOAL):
    frontier = [(heuristic(start), 0, start, [])]
    best_cost = {start: 0}

    while frontier:
        _, cost, state, path = heappop(frontier)
        if state == goal:
            return path + [state]
        if cost != best_cost.get(state):
            continue

        for next_state in neighbors(state):
            next_cost = cost + 1
            if next_cost < best_cost.get(next_state, float("inf")):
                best_cost[next_state] = next_cost
                heappush(
                    frontier,
                    (next_cost + heuristic(next_state), next_cost,
                     next_state, path + [state]),
                )
    return None


if __name__ == "__main__":
    solution = a_star()
    print("Moves:", len(solution) - 1 if solution else "No solution found")
