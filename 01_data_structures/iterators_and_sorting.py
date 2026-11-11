"""
Iterators, Data Aggregation, and Sorting Algorithms.

This module demonstrates core Python capabilities including iteration via zip/enumerate,
set operations, accumulator patterns, list comprehension filtering, and manual selection sort.
"""

# 1. Data Initialization
zahlen: list[int] = [1, 3, 5, 7, 9, 1, 13, 15, 2, 4, 6, 8, 10, 12, 14]
vornamen: list[str] = ["Akira", "Johanna", "Dave", "Egill", "Michelle", "Pierre"]
nachnamen: list[str] = [
    "Schmidt",
    "Petit",
    "Longbottom",
    "Grimsson",
    "Müller",
    "Nagata",
]

# 2. Sequence Pairing & Enumeration (die Sequenzverknüpfung)
namen: list[tuple[str, str]] = list(zip(vornamen, nachnamen))
print("Paired Names:", namen)

index_liste: list[tuple[int, tuple[str, str]]] = list(enumerate(namen, start=1))
print("Enumerated List:", index_liste)

print("=" * 40)

# 3. Iteration Variants (die Iterationsverfahren)
print("Standard Iteration:")
for vorname in vornamen:
    print(f"  Hallo {vorname}!")

print("\nUnordered Set Iteration:")
set_vornamen = set(vornamen)
for vorname in set_vornamen:
    print(f"  Hallo {vorname}!")

print("\nFormatted Indexed Output:")
for n, vorname in enumerate(vornamen, start=1):
    print(f"  {n}. {vorname.upper()}")

print("\nNumeric Power Range:")
for n in range(3, 12):
    print(f"  Square of {n}: {n**2}")

print("=" * 40)

# 4. Accumulation & Filtering (die Akkumulation und Filterung)
print(f"Built-in Sum: {sum(zahlen)}")

summe: int = 0
print("Cumulative Progression:")
for z in zahlen:
    summe += z
    print(f"  Current total: {summe}")

print("\nNon-multiples of 3:")
non_multiples = [z for z in zahlen if z % 3 != 0]
print(f"  Filtered list: {non_multiples}")

print("=" * 40)

# 5. Sorting Algorithms (der Sortieralgorithmus)
print(f"Built-in Sorted Copy: {sorted(zahlen)}")

# Manual Selection Sort Implementation (Corrected in-place swap)
for i in range(len(zahlen)):
    for j in range(i + 1, len(zahlen)):
        if zahlen[i] > zahlen[j]:
            zahlen[i], zahlen[j] = zahlen[j], zahlen[i]

print(f"In-place Sorted List: {zahlen}")
