"""Travelling Salesperson Problem — Hill Climbing and Simulated Annealing."""

import math
import random

CITIES = [(0, 0), (2, 4), (5, 2), (6, 6), (8, 3)]


def distance(city_a, city_b):
    return math.dist(CITIES[city_a], CITIES[city_b])


def tour_cost(tour):
    return sum(
        distance(tour[i], tour[(i + 1) % len(tour)])
        for i in range(len(tour))
    )


def neighbor(tour):
    candidate = tour[:]
    i, j = random.sample(range(len(candidate)), 2)
    candidate[i], candidate[j] = candidate[j], candidate[i]
    return candidate


def hill_climb(iterations=1000):
    current = list(range(len(CITIES)))
    random.shuffle(current)

    for _ in range(iterations):
        candidate = neighbor(current)
        if tour_cost(candidate) < tour_cost(current):
            current = candidate
    return current, tour_cost(current)


def simulated_annealing(iterations=1000, temperature=100, cooling=0.99):
    current = list(range(len(CITIES)))
    random.shuffle(current)
    current_cost = tour_cost(current)

    for _ in range(iterations):
        candidate = neighbor(current)
        candidate_cost = tour_cost(candidate)
        delta = candidate_cost - current_cost

        if delta < 0 or random.random() < math.exp(-delta / temperature):
            current, current_cost = candidate, candidate_cost
        temperature *= cooling
        if temperature <= 1e-12:
            break

    return current, current_cost


if __name__ == "__main__":
    hc_tour, hc_cost = hill_climb()
    sa_tour, sa_cost = simulated_annealing()
    print("HC Cost:", hc_cost, "Tour:", hc_tour)
    print("SA Cost:", sa_cost, "Tour:", sa_tour)
