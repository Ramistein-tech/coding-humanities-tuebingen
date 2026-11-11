"""
Data Structures Playground: Operations on Lists, Sets, and Tuples.
"""

start = "abcdefg"
print(list(start), set(start), tuple(start), sep="\n")

satz = [
    "Mit",
    "einem",
    "Xylophon",
    "kann",
    "man",
    "eigentlich",
    "zauberhaft",
    "Music",
    "machen",
]
halbsatz = ["wenn", "man", "ein", "wenig", "Begabung", "zeigt"]
sicherheitskopie = satz.copy()

print("--- Slicing Operations ---")
print(satz[2:4])
print(satz[:4])
print(satz[4:])
print(satz[::2])
print(satz[::-1])

print("\n--- List Modifications ---")
satz.extend(halbsatz)
satz.append("und")
satz.append("fleißig")
satz.append("ist")
print(satz)

print(f'\nAnzahl von "man": {satz.count("man")}')
print(f"Anzahl der Musikinstrumente: {satz.count('Xylophon')}")
print(f"Gesamtlänge: {len(satz)}")

satz.remove("eigentlich")
satz_sortiert = sorted(satz)
print(f"Sortiert: {satz_sortiert}")

satz.pop(10)
satz.pop(4)
satz.insert(2, "schönen und hochwertigen")
print(f"Endgültiger Satz: {satz}")

print("\n--- Sets & Aggregations ---")
würfelergebnisse = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
print(f"Einzigartige Werte (Set): {set(würfelergebnisse)}")
print(
    f"Min: {min(würfelergebnisse)}, Max: {max(würfelergebnisse)}, Summe: {sum(würfelergebnisse)}"
)

# تصحيح تحويل الـ Iterator إلى قائمة مطبوعة
testo = list(reversed(würfelergebnisse))
print(f"Reversed List: {testo}")
