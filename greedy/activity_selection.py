"""
Greedy Algorithm #1 — Activity Selection Problem
=================================================
Given a set of activities with start and finish times,
select the maximum number of non-overlapping activities.

Greedy Choice: Always pick the activity that finishes earliest
               (and doesn't conflict with the last selected one).

Time Complexity : O(n log n)  — dominated by sorting
Space Complexity: O(n)
"""

def activity_selection(activities: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Select the maximum set of non-overlapping activities.

    Parameters
    ----------
    activities : list of (start, finish) tuples

    Returns
    -------
    list of selected (start, finish) tuples
    """
    # Sort by finish time — core greedy decision
    sorted_acts = sorted(activities, key=lambda x: x[1])

    selected = [sorted_acts[0]]  # Always take the first (earliest finish)
    last_finish = sorted_acts[0][1]

    for start, finish in sorted_acts[1:]:
        if start >= last_finish:          # No overlap → greedy pick
            selected.append((start, finish))
            last_finish = finish

    return selected


def print_schedule(activities: list[tuple[int, int]], selected: list[tuple[int, int]]) -> None:
    print("\n📅  Activity Selection — Greedy Solution")
    print("=" * 45)
    print(f"{'Activity':<12} {'Start':>6} {'Finish':>8} {'Selected':>10}")
    print("-" * 45)
    for i, (s, f) in enumerate(activities):
        mark = "✔" if (s, f) in selected else " "
        print(f"  A{i+1:<9} {s:>6} {f:>8} {mark:>10}")
    print("-" * 45)
    print(f"  Max activities selected: {len(selected)}")


# ── Demo ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    activities = [
        (1, 4),   # A1
        (3, 5),   # A2
        (0, 6),   # A3
        (5, 7),   # A4
        (3, 9),   # A5
        (5, 9),   # A6
        (6, 10),  # A7
        (8, 11),  # A8
        (8, 12),  # A9
        (2, 14),  # A10
        (12, 16), # A11
    ]

    selected = activity_selection(activities)
    print_schedule(activities, selected)

    # Quick unit tests
    assert len(activity_selection([(1, 3), (2, 4), (3, 5)])) == 2
    assert len(activity_selection([(1, 2), (3, 4), (5, 6)])) == 3  # No overlaps
    assert len(activity_selection([(1, 10), (2, 3), (4, 5)])) == 2
    print("\n  All tests passed ✔")
