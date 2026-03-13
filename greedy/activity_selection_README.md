# Greedy Algorithm #1 — Activity Selection Problem

## Problem Statement

Given **n** activities, each with a **start time** and **finish time**, select the **maximum number of non-overlapping activities** that can be performed by a single person (or machine).

Two activities `i` and `j` are non-overlapping if `finish[i] ≤ start[j]` or `finish[j] ≤ start[i]`.

---

## Why Greedy Works Here

This is a classic **greedy** problem because a locally optimal choice leads to a globally optimal solution:

> **Greedy Rule:** Always select the activity with the **earliest finish time** that doesn't conflict with the previously selected activity.

**Intuition:** By finishing as early as possible, we leave the maximum remaining time open for future activities. Any other choice (e.g., earliest start, shortest duration) can be shown to produce suboptimal results.

**Proof sketch (Exchange Argument):**
Suppose there exists an optimal solution that does *not* include the earliest-finishing activity `a₁`. We can always swap the first activity in that optimal solution with `a₁` without reducing the total count, since `a₁` finishes no later than anything else.

---

## Algorithm Steps

```
1. Sort activities by finish time             O(n log n)
2. Select the first (earliest finish) activity
3. For each remaining activity (in sorted order):
      if start ≥ last_selected_finish:
          select it
          update last_selected_finish
4. Return selected activities
```

---

## Complexity

| Metric | Value |
|--------|-------|
| Time   | O(n log n) — sorting dominates |
| Space  | O(n) — sorted copy + result list |

---

## Example Walkthrough

Activities sorted by finish time:

| Activity | Start | Finish | Selected? |
|----------|-------|--------|-----------|
| A1       | 1     | 4      | ✔         |
| A2       | 3     | 5      | ✗ (3 < 4) |
| A3       | 0     | 6      | ✗ (0 < 4) |
| A4       | **5** | 7      | ✔ (5 ≥ 4) |
| A7       | **6** | 10     | ✗ (6 < 7) |
| A8       | **8** | 11     | ✔ (8 ≥ 7) |
| A11      | **12**| 16     | ✔ (12 ≥ 11)|

**Result:** 4 activities selected — A1, A4, A8, A11

---

## Running the Code

```bash
python activity_selection.py
```

**Expected output:**
```
📅  Activity Selection — Greedy Solution
=============================================
Activity      Start   Finish   Selected
---------------------------------------------
  A1            1        4          ✔
  A2            3        5
  ...
  Max activities selected: 4
```

---

## Real-World Applications

- **CPU Job Scheduling** — maximize number of tasks completed
- **Classroom/Resource Booking** — maximize room utilization
- **Sports Broadcasting** — schedule the most live games
- **Network Packet Scheduling** — maximize throughput

---

## Comparison with Brute Force

| Approach | Time Complexity | Notes |
|----------|----------------|-------|
| Brute Force | O(2ⁿ) | Check all subsets |
| Greedy (this) | O(n log n) | Optimal for this problem |
| Dynamic Programming | O(n²) | Overkill — greedy is sufficient |
