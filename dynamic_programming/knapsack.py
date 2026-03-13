"""
Dynamic Programming #1 — 0/1 Knapsack Problem
===============================================
Given n items each with a weight and value, and a knapsack with capacity W,
select items (each used at most once) to MAXIMIZE total value without
exceeding the weight limit.

DP Approach:
  - Subproblem: dp[i][w] = max value using first i items with capacity w
  - Transition: dp[i][w] = max(dp[i-1][w],  dp[i-1][w-weight[i]] + value[i])
  - Base case : dp[0][*] = 0  (no items → value 0)

Time Complexity : O(n × W)
Space Complexity: O(n × W)  /  O(W) with space optimization
"""


def knapsack(weights: list[int], values: list[int], capacity: int) -> tuple[int, list[int]]:
    """
    Solve the 0/1 Knapsack problem using bottom-up DP.

    Parameters
    ----------
    weights  : list of item weights
    values   : list of item values (same length as weights)
    capacity : maximum weight the knapsack can hold

    Returns
    -------
    (max_value, selected_items) where selected_items is a list of indices
    """
    n = len(weights)

    # Build DP table: dp[i][w] = best value using items 0..i-1 with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w_i = weights[i - 1]
        v_i = values[i - 1]
        for w in range(capacity + 1):
            # Option 1: Skip item i
            dp[i][w] = dp[i - 1][w]
            # Option 2: Take item i (if it fits)
            if w_i <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - w_i] + v_i)

    max_value = dp[n][capacity]

    # Backtrack to find which items were selected
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:   # Item i was included
            selected.append(i - 1)      # 0-indexed
            w -= weights[i - 1]
    selected.reverse()

    return max_value, selected


def knapsack_space_optimized(weights: list[int], values: list[int], capacity: int) -> int:
    """
    O(W) space version — only returns max value (no backtracking).
    Iterate capacity in REVERSE to avoid using the same item twice.
    """
    dp = [0] * (capacity + 1)
    for w_i, v_i in zip(weights, values):
        for w in range(capacity, w_i - 1, -1):   # Reverse pass!
            dp[w] = max(dp[w], dp[w - w_i] + v_i)
    return dp[capacity]


def print_table(dp: list[list[int]], weights: list[int], capacity: int) -> None:
    """Pretty-print the DP table."""
    n = len(dp) - 1
    print("\n  DP Table (rows = items, cols = capacity):")
    header = "  Item \\ W | " + " ".join(f"{w:3}" for w in range(capacity + 1))
    print(header)
    print("  " + "-" * (len(header) - 2))
    for i in range(n + 1):
        label = f"  {'base':>6}  | " if i == 0 else f"  item {i:>3}  | "
        row = " ".join(f"{dp[i][w]:3}" for w in range(capacity + 1))
        print(label + row)


# ── Demo ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Classic textbook example
    items = [
        {"name": "Laptop",     "weight": 3, "value": 4},
        {"name": "Headphones", "weight": 4, "value": 5},
        {"name": "Book",       "weight": 2, "value": 3},
        {"name": "Phone",      "weight": 1, "value": 2},
        {"name": "Tablet",     "weight": 5, "value": 7},
    ]
    capacity = 7

    weights = [item["weight"] for item in items]
    values  = [item["value"]  for item in items]

    # Build full table for display
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])

    print("=" * 55)
    print("  0/1 Knapsack — Dynamic Programming")
    print("=" * 55)
    print(f"\n  Capacity: {capacity} kg")
    print(f"\n  {'#':<4} {'Item':<14} {'Weight':>7} {'Value':>7}")
    print(f"  {'-'*36}")
    for i, item in enumerate(items):
        print(f"  {i+1:<4} {item['name']:<14} {item['weight']:>6}kg {item['value']:>6}$")

    print_table(dp, weights, capacity)

    max_val, selected = knapsack(weights, values, capacity)
    total_w = sum(weights[i] for i in selected)

    print(f"\n  ✅ Selected Items:")
    for i in selected:
        print(f"     • {items[i]['name']:<14} {weights[i]}kg  ${values[i]}")
    print(f"\n  Total Weight : {total_w} / {capacity} kg")
    print(f"  Total Value  : ${max_val}")

    # Verify space-optimized gives same answer
    assert knapsack_space_optimized(weights, values, capacity) == max_val

    # Unit tests
    assert knapsack([1, 2, 3], [6, 10, 12], 5) == (22, [1, 2])
    assert knapsack([10], [60], 5) == (0, [])
    assert knapsack([1], [100], 1) == (100, [0])

    print("\n  All tests passed ✔")
