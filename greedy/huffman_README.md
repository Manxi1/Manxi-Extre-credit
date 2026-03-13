# Greedy Algorithm #2 — Huffman Encoding

## Problem Statement

Given a set of symbols and their **frequencies**, assign a **prefix-free binary code** to each symbol such that the **total encoded length is minimized**.

A prefix-free code guarantees no codeword is a prefix of another, enabling unambiguous decoding.

---

## Why Greedy Works Here

**Greedy Rule:** At every step, merge the **two nodes with the lowest frequency** into a new internal node.

**Intuition:** Symbols that appear more frequently should have shorter codes. By always combining the rarest symbols first, we push them deeper into the tree (longer codes) while frequent symbols naturally rise toward the root (shorter codes).

**Proof of Optimality (Huffman, 1952):**
The greedy choice is safe because any optimal code tree must have the two least-frequent symbols as the deepest siblings. Swapping them with any other pair cannot improve the cost — it can only make it worse or keep it the same.

---

## Algorithm Steps

```
1. Create a leaf node for each symbol and add to a min-heap
2. While heap has more than 1 node:
      a. Pop the two nodes with lowest frequency  →  lo, hi
      b. Create internal node with freq = lo.freq + hi.freq
      c. Set lo as left child, hi as right child
      d. Push new node back into the heap
3. The remaining node is the root of the Huffman tree
4. Traverse tree: left edge = '0', right edge = '1'
```

---

## Complexity

| Metric | Value |
|--------|-------|
| Time   | O(n log n) — n heap operations × O(log n) each |
| Space  | O(n) — heap + tree nodes |

---

## Example Walkthrough

Input: `"aabbbccccdddddd"` → frequencies: `{a:2, b:3, c:4, d:6}`

**Building the tree:**
```
Step 1: Heap = [a:2, b:3, c:4, d:6]
Step 2: Merge a+b → [ab:5, c:4, d:6]
Step 3: Merge c+ab → [cab:9, d:6]  (heap reorders to [d:6, cab:9])
Step 4: Merge d+cab → root:15
```

**Resulting codes:**
```
d → 0       (freq 6, 1 bit)
c → 10      (freq 4, 2 bits)
b → 110     (freq 3, 3 bits)
a → 111     (freq 2, 3 bits)
```

**Comparison:**
| Method | Bits Used |
|--------|-----------|
| Fixed-width (2 bits/symbol) | 30 bits |
| Huffman | 6×1 + 4×2 + 3×3 + 2×3 = **29 bits** |

---

## Tree Visualization

```
          [15]
         /    \
       [6]   [9]
        d    /  \
           [5]  [4]
           / \    c
          [2][3]
           a   b
```

---

## Running the Code

```bash
python huffman.py
```

**Expected output:**
```
🗜️  Huffman Encoding — Greedy Solution
====================================================
  Symbol    Freq  Code             Bits
----------------------------------------------------
  ' '          6  000                3
  a            3  ...
  ...
  Space savings: ~XX%
```

---

## Real-World Applications

- **ZIP / DEFLATE compression** — core of most file compression
- **JPEG image compression** — entropy coding stage
- **MP3 audio** — Huffman codes in the bitstream
- **HTTP/2 HPACK** — header compression

---

## Key Properties

| Property | Explanation |
|----------|-------------|
| Prefix-free | No codeword is a prefix of another |
| Lossless | Original data recoverable exactly |
| Optimal | Minimum expected bits among all prefix-free codes |
| Greedy | Local choice (merge smallest) → global optimum |
