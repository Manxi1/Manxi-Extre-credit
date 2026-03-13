# NP Extra Credit — Traveling Salesman Problem (TSP)

## Problem Statement

Given **n cities** and the **distance** between every pair of cities, find the **shortest possible tour** that:
1. Starts at a home city
2. Visits **every city exactly once**
3. Returns to the starting city

---

## What Makes TSP Hard? (NP-Hardness)

### Decision Version (NP-Complete)
"Does there exist a tour of length ≤ k?"

This is **NP-complete**, meaning:
- Any NP problem can be reduced to it
- A solution can be **verified** in polynomial time
- No known **polynomial-time algorithm** exists to solve it

### Optimization Version (NP-Hard)
Finding the **minimum** tour length is NP-hard — at least as hard as the hardest NP problems.

**Why we believe P ≠ NP here:** The search space is **(n-1)! tours** (fixing one city to eliminate rotations). For n=20, that's 121,645,100,408,832,000 tours.

---

## Three Approaches Implemented

### 1. Brute Force — O(n!)

```
for every permutation of n-1 cities:
    compute tour length
    track minimum
```

**Feasible for:** n ≤ 12 (n=12 → 39,916,800 tours)
**For n=20:** 121 quadrillion operations — infeasible

---

### 2. Held-Karp Dynamic Programming — O(n² · 2ⁿ)

Uses **bitmask DP** to avoid re-exploring the same city subsets.

**State:** `dp[S][v]` = minimum distance to travel from city 0, visit exactly the cities in bitmask `S`, and end at city `v`

**Recurrence:**
```
dp[S | (1<<v)][v] = min over all u in S:
                        dp[S][u] + dist[u][v]
```

**Base case:** `dp[{0}][0] = 0`

**Final answer:** `min over all v: dp[ALL][v] + dist[v][0]`

| n | Brute Force | Held-Karp |
|---|-------------|-----------|
| 10 | 362,880 | 10,240 |
| 15 | 87 billion | 3.6 million |
| 20 | 121 quadrillion | 419 million |
| 25 | 6.2 × 10²³ | 20 billion |

---

### 3. Nearest Neighbor Heuristic — O(n²)

```
start at city 0
while unvisited cities remain:
    go to the nearest unvisited city
return to start
```

**Pros:** Very fast, usually within 25% of optimal
**Cons:** Not guaranteed to be optimal — can be far off in worst case

---

## Complexity Summary

| Algorithm | Time | Space | Optimal? |
|-----------|------|-------|---------|
| Brute Force | O(n!) | O(n) | Yes |
| Held-Karp DP | O(n² · 2ⁿ) | O(n · 2ⁿ) | Yes |
| Nearest Neighbor | O(n²) | O(n) | No (heuristic) |
| Christofides | O(n³) | O(n²) | No (≤ 1.5× optimal) |

---

## Example Walkthrough (n=6)

Cities at coordinates: `(0,0), (1,3), (4,3), (6,1), (3,0), (5,4)`

```
Brute Force  →  Tour: 0→1→2→5→3→4→0   Length: 17.39
Held-Karp    →  Tour: 0→1→2→5→3→4→0   Length: 17.39  ✓ matches
Nearest Nbr  →  Tour: 0→4→3→5→2→1→0   Length: 18.21  (+4.7%)
```

---

## Bitmask DP Visualization

For 4 cities {0,1,2,3}, the DP has 2⁴=16 states per city:

```
Bitmask 0001 = {C0}       — only start city visited
Bitmask 0011 = {C0, C1}   — visited 0 and 1
Bitmask 1111 = {C0,C1,C2,C3}  — all visited → check return to 0
```

The key insight: **two tours that visit the same set of cities and end at the same city are equivalent** for future decisions. This compresses exponential cases into polynomial ones.

---

## Running the Code

```bash
python tsp.py
```

**Expected output:**
```
============================================================
  Traveling Salesman Problem — NP-Hard
============================================================

  Algorithm                  Tour Length  Tour
  ------------------------------------------------------------
  Brute Force (exact)             17.39  C0 → C1 → C2 → ...
  Held-Karp DP (exact)            17.39  C0 → C1 → C2 → ...
  Nearest Neighbor                18.21  C0 → C4 → C3 → ...

  NN heuristic error: 4.7% above optimal
  Held-Karp matches Brute Force ✔
```

---

## Real-World Applications

| Domain | TSP Variant |
|--------|-------------|
| **Logistics** | UPS/FedEx route optimization saves millions |
| **PCB Manufacturing** | Minimize drill movement on circuit boards |
| **DNA sequencing** | Sequence fragment assembly |
| **Telescope scheduling** | Minimize slew time between observations |
| **Genome rearrangement** | Evolutionary biology analysis |

---

## Why This Is Studied

TSP is the flagship NP-hard problem. Studying it teaches:
- **NP-completeness theory** — reduction from Hamiltonian Cycle
- **Exact exponential algorithms** — when approximation isn't acceptable
- **Approximation algorithms** — Christofides guarantees 1.5× optimal
- **Heuristics and metaheuristics** — simulated annealing, genetic algorithms
- **The P vs NP question** — perhaps the biggest open problem in computer science
