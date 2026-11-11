"""
Stochastic Data Sampling and Iterative Process Automation.

This module demonstrates sequence pairing via zip(), random single-element access
(der stochastische Zugriff), and complete data structure traversal (die Prozessautomatisierung)
for text data prep pipelines in Natural Language Processing (NLP).
"""

import random

# 1. Initialization & Data Preparation (die Datenvorbereitung)
vornamen: list[str] = ["Akira", "Johanna", "Dave", "Egill", "Michelle", "Pierre"]
nachnamen: list[str] = [
    "Schmidt",
    "Petit",
    "Longbottom",
    "Grimsson",
    "Müller",
    "Nagata",
]

# Randomization and Tuple Creation
random.shuffle(vornamen)
random.shuffle(nachnamen)
namen: list[tuple[str, str]] = list(zip(vornamen, nachnamen))

# ==============================================================================
# Teil 1: Der stochastische Zugriff (الوصول التصادفي / العشوائي)
# ==============================================================================
# Nutzt einen mathematischen Zufall, um einmalig zuzugreifen.
# Hier verwenden wir random.randint(), um exakt einen Zufallsindex (فهرس عشوائي) zu wählen.
# Der Code nutzt den Direktzugriff (الوصول المباشر) auf das Datenelement.
# Der Rest der Liste bleibt im Speicher, wird aber mangels Iterationsbefehl nicht gedruckt.

i: int = random.randint(0, len(namen) - 1)
zufalls_vorname, zufalls_nachname = namen[i]

print("=" * 70)
print(f"EINZELZUGRIFF (Index {i}):")
print(
    f"Nachname: {zufalls_nachname}, Vorname: {zufalls_vorname}; "
    f"also {zufalls_vorname} {zufalls_nachname}"
)
print("=" * 70)

# ==============================================================================
# Teil 2: Die Prozessautomatisierung (أتمتة العملية عبر التكرار)
# ==============================================================================
# Eine for-Schleife zwingt den Computer zu einer systematischen Wiederholung
# (die Iteration - التكرار المتسلسل).
# Der Code stoppt nicht nach einem Element, sondern führt das Durchlaufen der Datenstruktur
# (اجتياز بنية البيانات) aus, bis jedes einzelne Element/Tupel verarbeitet ist.

print("\nDie vollständige Namensliste (Prozessautomatisierung):")
print("-" * 70)

for vorname, nachname in namen:
    print(f"Nachname: {nachname}, Vorname: {vorname}; also {vorname} {nachname}.")

print("=" * 70)
