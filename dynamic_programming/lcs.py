"""
Dynamic Programming #2 — Longest Common Subsequence (LCS)
===========================================================
Given two sequences X and Y, find the length of their longest
common subsequence — a sequence that appears in both X and Y
(not necessarily contiguous, but in the same order).

DP Approach:
  Subproblem : lcs(i, j) = LCS length of X[0..i-1] and Y[0..j-1]
  Transition :
    if X[i-1] == Y[j-1]:  dp[i][j] = dp[i-1][j-1] + 1
    else:                  dp[i][j] = max(dp[i-1][j], dp[i][j-1])
  Base case  : dp[0][*] = dp[*][0] = 0

Time Complexity : O(m × n)
Space Complexity: O(m × n)  /  O(min(m,n)) space-optimized
"""


def lcs_length(X: str, Y: str) -> int:
    """Return just the length of the LCS — O(m×n) time, O(m×n) space."""
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def lcs(X: str, Y: str) -> tuple[int, str]:
    """
    Find the LCS length AND reconstruct the actual subsequence.

    Parameters
    ----------
    X, Y : input strings

    Returns
    -------
    (length, lcs_string)
    """
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to reconstruct the LCS string
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            result.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j += -1

    return dp[m][n], "".join(reversed(result))


def lcs_space_optimized(X: str, Y: str) -> int:
    """O(min(m,n)) space using two rows."""
    if len(X) < len(Y):
        X, Y = Y, X          # Ensure Y is shorter
    n = len(Y)
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    for ch_x in X:
        for j in range(1, n + 1):
            if ch_x == Y[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, [0] * (n + 1)

    return prev[n]


def print_table(X: str, Y: str, dp: list[list[int]]) -> None:
    """Pretty-print the DP table."""
    print(f"\n  DP Table:")
    print(f"         {'  '.join(['ε'] + list(Y))}")
    print(f"      {'  '.join([str(c) for c in range(len(Y)+1)])}")
    print(f"  {'─' * (len(Y) * 3 + 8)}")
    for i, row_label in enumerate(['ε'] + list(X)):
        row = "  ".join(str(dp[i][j]) for j in range(len(Y) + 1))
        print(f"  {row_label}  {i}  {row}")


def diff_style(X: str, Y: str, common: str) -> None:
    """Show which characters are in common visually."""
    print(f"\n  X: ", end="")
    ci = 0
    for ch in X:
        if ci < len(common) and ch == common[ci]:
            print(f"\033[92m{ch}\033[0m", end="")  # Green
            ci += 1
        else:
            print(ch, end="")
    print()
    print(f"  Y: ", end="")
    ci = 0
    for ch in Y:
        if ci < len(common) and ch == common[ci]:
            print(f"\033[92m{ch}\033[0m", end="")
            ci += 1
        else:
            print(ch, end="")
    print()


# ── Demo ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  Longest Common Subsequence — Dynamic Programming")
    print("=" * 55)

    pairs = [
        ("ABCBDAB", "BDCABA"),
        ("AGGTAB",  "GXTXAYB"),
        ("intention", "execution"),
    ]

    for X, Y in pairs:
        length, common = lcs(X, Y)
        print(f"\n  X = \"{X}\"")
        print(f"  Y = \"{Y}\"")
        print(f"  LCS = \"{common}\"  (length {length})")

    # Table demo for small input
    X, Y = "ABCB", "BDCAB"
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(f"\n  [Detailed table for X=\"{X}\", Y=\"{Y}\"]")
    print_table(X, Y, dp)

    # Unit tests
    assert lcs("ABCBDAB", "BDCABA")[0] == 4
    assert lcs("AGGTAB", "GXTXAYB")[0] == 4
    assert lcs("", "ABC")[0] == 0
    assert lcs("AAA", "AA")[0] == 2
    assert lcs_space_optimized("ABCBDAB", "BDCABA") == 4

    print("\n  All tests passed ✔")
