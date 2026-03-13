"""
Greedy Algorithm #2 — Huffman Encoding
=======================================
Build an optimal prefix-free binary encoding for a set of symbols
by greedily merging the two least-frequent nodes at every step.

Greedy Choice: Always combine the two nodes with the LOWEST frequency.
               This ensures high-frequency symbols get shorter codes.

Time Complexity : O(n log n)  — n heap operations each O(log n)
Space Complexity: O(n)
"""

import heapq
from dataclasses import dataclass, field
from typing import Optional


# ── Tree Node ────────────────────────────────────────────────────────────────

@dataclass(order=True)
class HuffNode:
    freq: int
    symbol: Optional[str] = field(default=None, compare=False)
    left:  Optional["HuffNode"] = field(default=None, compare=False)
    right: Optional["HuffNode"] = field(default=None, compare=False)

    @property
    def is_leaf(self) -> bool:
        return self.symbol is not None


# ── Core Algorithm ───────────────────────────────────────────────────────────

def build_huffman_tree(freq_table: dict[str, int]) -> HuffNode:
    """
    Build the Huffman tree using a min-heap.

    Parameters
    ----------
    freq_table : {symbol: frequency}

    Returns
    -------
    Root HuffNode of the completed tree
    """
    heap = [HuffNode(freq=f, symbol=s) for s, f in freq_table.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        # Greedy: merge the two smallest
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        merged = HuffNode(freq=lo.freq + hi.freq, left=lo, right=hi)
        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(node: HuffNode, prefix: str = "", codes: dict | None = None) -> dict[str, str]:
    """Traverse the tree to collect binary codes for each symbol."""
    if codes is None:
        codes = {}
    if node.is_leaf:
        codes[node.symbol] = prefix or "0"  # Edge case: single symbol
    else:
        if node.left:
            generate_codes(node.left,  prefix + "0", codes)
        if node.right:
            generate_codes(node.right, prefix + "1", codes)
    return codes


def encode(text: str, codes: dict[str, str]) -> str:
    return "".join(codes[ch] for ch in text)


def decode(bits: str, root: HuffNode) -> str:
    result = []
    node = root
    for bit in bits:
        node = node.left if bit == "0" else node.right
        if node.is_leaf:
            result.append(node.symbol)
            node = root
    return "".join(result)


# ── Display Helpers ──────────────────────────────────────────────────────────

def print_codes(freq_table: dict[str, int], codes: dict[str, str]) -> None:
    print("\n🗜️  Huffman Encoding — Greedy Solution")
    print("=" * 52)
    print(f"  {'Symbol':<8} {'Freq':>6} {'Code':<16} {'Bits':>4}")
    print("-" * 52)
    total_bits = sum(freq_table[s] * len(c) for s, c in codes.items())
    fixed_bits = sum(freq_table[s] for s in freq_table) * len(bin(len(freq_table))[2:])
    for sym, code in sorted(codes.items(), key=lambda x: len(x[1])):
        display = repr(sym) if sym == " " else sym
        print(f"  {display:<8} {freq_table[sym]:>6} {code:<16} {len(code):>4}")
    print("-" * 52)
    print(f"  Huffman bits  : {total_bits}")
    print(f"  Fixed-width   : {fixed_bits}  ({len(bin(len(freq_table))[2:])} bits/symbol)")
    pct = (1 - total_bits / fixed_bits) * 100 if fixed_bits > 0 else 0
    print(f"  Space savings : {pct:.1f}%")


# ── Demo ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    text = "this is an example of a huffman tree"

    # Build frequency table
    freq_table: dict[str, int] = {}
    for ch in text:
        freq_table[ch] = freq_table.get(ch, 0) + 1

    root  = build_huffman_tree(freq_table)
    codes = generate_codes(root)

    print_codes(freq_table, codes)

    # Round-trip test
    encoded = encode(text, codes)
    decoded = decode(encoded, root)
    print(f"\n  Original : {text}")
    print(f"  Encoded  : {encoded[:60]}...")
    print(f"  Decoded  : {decoded}")
    assert decoded == text, "Round-trip failed!"
    print("\n  Round-trip test passed ✔")
