"""
NP Extra Credit — Traveling Salesman Problem (TSP)
====================================================
Given n cities and distances between every pair of cities,
find the SHORTEST tour that visits every city exactly once
and returns to the starting city.

This file implements THREE approaches to compare:

  1. Brute Force           — O(n!)      exact, impractical for n > 12
  2. Dynamic Programming   — O(n² 2ⁿ)  exact via Held-Karp algorithm
  3. Nearest Neighbor      — O(n²)      greedy heuristic, not always optimal

TSP is NP-hard: no known polynomial-time exact algorithm exists.
It is NP-complete in its decision form: "Is there a tour of length ≤ k?"
"""

import math
import itertools
from typing import Optional


# ── Distance Helpers ─────────────────────────────────────────────────────────

def euclidean_dist(a: tuple[float, float], b: tuple[float, float]) -> float:
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def build_distance_matrix(cities: list[tuple[float, float]]) -> list[list[float]]:
    n = len(cities)
    return [[euclidean_dist(cities[i], cities[j]) for j in range(n)] for i in range(n)]


def tour_length(tour: list[int], dist: list[list[float]]) -> float:
    return sum(dist[tour[i]][tour[(i + 1) % len(tour)]] for i in range(len(tour)))


# ── Approach 1: Brute Force ─────────────────────────────────────────────────

def tsp_brute_force(dist: list[list[float]]) -> tuple[float, list[int]]:
    """
    Try every permutation of cities.
    Exact but only feasible for n ≤ ~12.

    Time: O(n!)
    """
    n = len(dist)
    cities = list(range(1, n))    # Fix city 0 as start to eliminate rotations
    best_length = math.inf
    best_tour   = []

    for perm in itertools.permutations(cities):
        tour = [0] + list(perm)
        length = tour_length(tour, dist)
        if length < best_length:
            best_length = length
            best_tour   = tour[:]

    return best_length, best_tour


# ── Approach 2: Held-Karp DP (Exact) ────────────────────────────────────────

def tsp_held_karp(dist: list[list[float]]) -> tuple[float, list[int]]:
    """
    Held-Karp dynamic programming algorithm.
    Exact solution with bitmask DP.

    State: dp[S][v] = shortest path visiting exactly the cities in bitmask S,
                      ending at city v, starting from city 0.

    Time:  O(n² · 2ⁿ)
    Space: O(n · 2ⁿ)
    """
    n = len(dist)
    INF = math.inf
    FULL = (1 << n) - 1    # All cities visited

    # dp[mask][v] = min cost to reach v having visited cities in mask
    dp     = [[INF] * n for _ in range(1 << n)]
    parent = [[-1]  * n for _ in range(1 << n)]

    dp[1][0] = 0.0          # Start at city 0 (mask = 0b0001)

    for mask in range(1, 1 << n):
        if not (mask & 1):  # Must include city 0
            continue
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            if dp[mask][u] == INF:
                continue
            for v in range(n):
                if mask & (1 << v):   # Already visited
                    continue
                new_mask = mask | (1 << v)
                new_cost = dp[mask][u] + dist[u][v]
                if new_cost < dp[new_mask][v]:
                    dp[new_mask][v]     = new_cost
                    parent[new_mask][v] = u

    # Find best final city before returning to 0
    best_length = INF
    last_city   = -1
    for v in range(1, n):
        cost = dp[FULL][v] + dist[v][0]
        if cost < best_length:
            best_length = cost
            last_city   = v

    # Reconstruct tour via parent pointers
    tour = []
    mask = FULL
    curr = last_city
    while curr != -1:
        tour.append(curr)
        prev = parent[mask][curr]
        mask ^= (1 << curr)
        curr = prev
    tour.reverse()

    return best_length, tour


# ── Approach 3: Nearest Neighbor Heuristic ──────────────────────────────────

def tsp_nearest_neighbor(dist: list[list[float]], start: int = 0) -> tuple[float, list[int]]:
    """
    Greedy heuristic: always go to the nearest unvisited city.

    Not always optimal, but runs in O(n²) — good approximation.
    """
    n = len(dist)
    visited = [False] * n
    tour    = [start]
    visited[start] = True

    for _ in range(n - 1):
        curr = tour[-1]
        nearest = min(
            (j for j in range(n) if not visited[j]),
            key=lambda j: dist[curr][j]
        )
        tour.append(nearest)
        visited[nearest] = True

    return tour_length(tour, dist), tour


# ── Demo ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # 6-city example with (x,y) coordinates
    cities = [
        (0, 0),    # City 0
        (1, 3),    # City 1
        (4, 3),    # City 2
        (6, 1),    # City 3
        (3, 0),    # City 4
        (5, 4),    # City 5
    ]

    dist = build_distance_matrix(cities)
    n = len(cities)

    print("=" * 60)
    print("  Traveling Salesman Problem — NP-Hard")
    print("=" * 60)

    print("\n  Cities:")
    for i, (x, y) in enumerate(cities):
        print(f"    City {i}: ({x}, {y})")

    print(f"\n  Distance Matrix:")
    print(f"       {'  '.join(f'  C{i}' for i in range(n))}")
    for i in range(n):
        row = "  ".join(f"{dist[i][j]:4.1f}" for j in range(n))
        print(f"  C{i}   {row}")

    # Run all three approaches
    bf_len,  bf_tour  = tsp_brute_force(dist)
    hk_len,  hk_tour  = tsp_held_karp(dist)
    nn_len,  nn_tour  = tsp_nearest_neighbor(dist)

    def fmt_tour(tour):
        return " → ".join(f"C{c}" for c in tour) + f" → C{tour[0]}"

    print(f"\n  {'Algorithm':<25} {'Tour Length':>12}  {'Tour'}")
    print(f"  {'-'*60}")
    print(f"  {'Brute Force (exact)':<25} {bf_len:>12.2f}  {fmt_tour(bf_tour)}")
    print(f"  {'Held-Karp DP (exact)':<25} {hk_len:>12.2f}  {fmt_tour(hk_tour)}")
    print(f"  {'Nearest Neighbor':<25} {nn_len:>12.2f}  {fmt_tour(nn_tour)}")

    nn_error = (nn_len - bf_len) / bf_len * 100
    print(f"\n  NN heuristic error: {nn_error:.1f}% above optimal")

    # Verify Held-Karp matches brute force
    assert abs(hk_len - bf_len) < 1e-9, "Held-Karp should match brute force!"
    print("\n  Held-Karp matches Brute Force ✔")

    # Complexity comparison
    print(f"\n  Complexity at n=20:")
    print(f"    Brute Force   : {math.factorial(19):,} ops  (≈ 1.2 × 10¹⁷)")
    print(f"    Held-Karp DP  : {20**2 * 2**20:,} ops  (≈ 4 × 10⁸)")
    print(f"    Nearest Nbr   : {20**2} ops")
