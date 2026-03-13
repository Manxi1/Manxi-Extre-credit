"""
Divide & Conquer #2 — Binary Search
======================================
Search a SORTED array for a target by repeatedly halving the
search space until the target is found or ruled out.

D&C Structure:
  Divide  : Compute the midpoint                  O(1)
  Conquer : Recurse on ONE half (not both)         T(n/2)
  Combine : No merging needed — answer is direct   O(1)

Time Complexity : O(log n)
Space Complexity: O(1) iterative  /  O(log n) recursive (call stack)
"""


# ── Iterative (preferred — no stack overhead) ────────────────────────────────

def binary_search(arr: list, target) -> int:
    """
    Find the index of target in a sorted array, or -1 if not present.

    Parameters
    ----------
    arr    : sorted list of comparable elements
    target : value to search for

    Returns
    -------
    Index of target in arr, or -1
    """
    lo, hi = 0, len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2        # Divide: pick midpoint

        if arr[mid] == target:      # Found
            return mid
        elif arr[mid] < target:     # Conquer right half
            lo = mid + 1
        else:                       # Conquer left half
            hi = mid - 1

    return -1                       # Not found


# ── Recursive (classic D&C form) ─────────────────────────────────────────────

def binary_search_recursive(arr: list, target, lo: int = 0, hi: int | None = None) -> int:
    """Recursive binary search — pure D&C formulation."""
    if hi is None:
        hi = len(arr) - 1

    if lo > hi:                     # Base case: empty range
        return -1

    mid = (lo + hi) // 2           # Divide

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, hi)   # Conquer right
    else:
        return binary_search_recursive(arr, target, lo, mid - 1)   # Conquer left


# ── Extensions ───────────────────────────────────────────────────────────────

def lower_bound(arr: list, target) -> int:
    """
    Find the leftmost index where target could be inserted to keep arr sorted.
    (Equivalent to C++ lower_bound / Python bisect_left)
    """
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(arr: list, target) -> int:
    """
    Find the rightmost index where target could be inserted (bisect_right).
    """
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def count_occurrences(arr: list, target) -> int:
    """Count how many times target appears in the sorted array."""
    return upper_bound(arr, target) - lower_bound(arr, target)


# ── Tracing search ───────────────────────────────────────────────────────────

def binary_search_traced(arr: list, target) -> int:
    """Binary search with step-by-step output."""
    lo, hi = 0, len(arr) - 1
    step = 1
    print(f"\n  Searching for {target} in {arr}")
    print(f"  {'Step':<6} {'lo':>4} {'hi':>4} {'mid':>4} {'arr[mid]':>10} {'Action'}")
    print(f"  {'-'*50}")

    while lo <= hi:
        mid = (lo + hi) // 2
        action = ""
        if arr[mid] == target:
            action = "FOUND ✔"
        elif arr[mid] < target:
            action = "go right →"
            lo = mid + 1
        else:
            action = "← go left"
            hi = mid - 1
        print(f"  {step:<6} {lo-(1 if arr[mid]<target else 0):>4} {hi+(1 if arr[mid]>target else 0):>4} {mid:>4} {arr[mid]:>10}  {action}")
        if arr[mid] == target:
            return mid
        step += 1

    print(f"  → Not found")
    return -1


# ── Demo ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import random

    print("=" * 52)
    print("  Binary Search — Divide & Conquer")
    print("=" * 52)

    arr = sorted(random.sample(range(1, 100), 15))
    target = arr[5]
    missing = 999

    binary_search_traced(arr, target)
    binary_search_traced(arr, missing)

    # Correctness tests
    for val in arr:
        idx = binary_search(arr, val)
        assert arr[idx] == val, f"Failed for {val}"
    assert binary_search(arr, -1) == -1
    assert binary_search([], 5) == -1
    assert binary_search([5], 5) == 0

    # count_occurrences
    dupes = [1, 2, 2, 2, 3, 4]
    assert count_occurrences(dupes, 2) == 3
    assert count_occurrences(dupes, 5) == 0

    print("\n  All tests passed ✔")
