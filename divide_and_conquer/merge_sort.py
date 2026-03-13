"""
Divide & Conquer #1 — Merge Sort
==================================
Recursively split an array in half, sort each half, then merge
the sorted halves back together.

D&C Structure:
  Divide  : Split array into two halves          O(1)
  Conquer : Recursively sort each half            T(n/2) × 2
  Combine : Merge two sorted arrays               O(n)

Time Complexity : O(n log n)  — all cases (worst, avg, best)
Space Complexity: O(n)        — auxiliary array for merging
"""


def merge_sort(arr: list) -> list:
    """
    Return a new sorted list using merge sort.

    Parameters
    ----------
    arr : list of comparable elements

    Returns
    -------
    Sorted list
    """
    if len(arr) <= 1:          # Base case
        return arr

    mid   = len(arr) // 2
    left  = merge_sort(arr[:mid])   # Conquer left half
    right = merge_sort(arr[mid:])   # Conquer right half

    return _merge(left, right)       # Combine


def _merge(left: list, right: list) -> list:
    """Merge two sorted lists into one sorted list — O(n)."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ── In-place variant (for reference) ────────────────────────────────────────

def merge_sort_inplace(arr: list, lo: int = 0, hi: int | None = None) -> None:
    """In-place merge sort (modifies arr directly)."""
    if hi is None:
        hi = len(arr) - 1
    if lo >= hi:
        return
    mid = (lo + hi) // 2
    merge_sort_inplace(arr, lo, mid)
    merge_sort_inplace(arr, mid + 1, hi)
    _merge_inplace(arr, lo, mid, hi)


def _merge_inplace(arr: list, lo: int, mid: int, hi: int) -> None:
    left  = arr[lo : mid + 1]
    right = arr[mid + 1 : hi + 1]
    i = j = 0
    k = lo
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]; i += 1
        else:
            arr[k] = right[j]; j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]; i += 1; k += 1
    while j < len(right):
        arr[k] = right[j]; j += 1; k += 1


# ── Tracing variant (educational) ───────────────────────────────────────────

def merge_sort_traced(arr: list, depth: int = 0) -> list:
    """Same as merge_sort but prints each recursive call."""
    indent = "  " * depth
    print(f"{indent}↓ split  {arr}")
    if len(arr) <= 1:
        print(f"{indent}↑ base   {arr}")
        return arr
    mid   = len(arr) // 2
    left  = merge_sort_traced(arr[:mid], depth + 1)
    right = merge_sort_traced(arr[mid:], depth + 1)
    merged = _merge(left, right)
    print(f"{indent}↑ merge  {merged}")
    return merged


# ── Demo ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import random

    print("=" * 50)
    print("  Merge Sort — Divide & Conquer")
    print("=" * 50)

    # Trace a small example
    print("\n[Traced execution on [5, 3, 8, 1, 9, 2]]")
    result = merge_sort_traced([5, 3, 8, 1, 9, 2])
    print(f"\nFinal sorted: {result}")

    # Large random test
    data = random.sample(range(1000), 20)
    print(f"\n[Large test]\nInput : {data}")
    print(f"Output: {merge_sort(data)}")

    # Edge cases
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([2, 1]) == [1, 2]
    assert merge_sort([3, 3, 1, 2]) == [1, 2, 3, 3]

    # Strings
    words = ["banana", "apple", "cherry", "date"]
    assert merge_sort(words) == sorted(words)

    print("\n  All tests passed ✔")
