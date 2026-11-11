# ==============================================================================
# Erstellung einer formatierten Tabelle mit verschachtelten for-Schleifen.
# ==============================================================================

"""
ALLGEMEINE ERKLÄRUNG:
Dieses Skript generiert eine 10x10 Multiplikationstabelle.
Es nutzt "verschachtelte Schleifen" (Nested Loops) und "String-Formatierung"
(f-Strings mit Platzhaltern), um die Zahlen wie in einem echten Raster (Matrix)
perfekt untereinander auszurichten.
"""

# ------------------------------------------------------------------------------
# 1. KOPFZEILE (Die oberste Zahlenreihe generieren)
# ------------------------------------------------------------------------------
# WARUM: Wir brauchen eine saubere Ausrichtung. Die obere linke Ecke der
# Tabelle bleibt leer, gefolgt von einem vertikalen Trennstrich '|'.
# WIE: f"{'':3}" erzeugt genau 3 leere Leerzeichen.
# end="" verhindert, dass Python automatisch in eine neue Zeile springt.
print(f"{'':3} |", end="")

# Wir nutzen eine for-Schleife, um die Spaltenzahlen (1 bis 10) zu drucken.
# range(1, 11) bedeutet: Starte bei 1 und höre VOR 11 auf (also bei 10).
for spalte in range(1, 11):
    # f"{spalte:4}" bedeutet: Reserviere genau 4 Zeichenplätze für diese Zahl.
    # Dadurch werden alle Zahlen rechtsbündig (rechtsbündige Ausrichtung) ausgerichtet.
    print(f"{spalte:4}", end="")

# Nach der Schleife drucken wir ein leeres print(), um einen Zeilenumbruch
# (Enter / Line Break) zu erzeugen und in die nächste Zeile zu springen.
print()


# ------------------------------------------------------------------------------
# 2. TRENNLINIE (Die gestrichelte Linie unter der Kopfzeile)
# ------------------------------------------------------------------------------
# In Python können wir Strings einfach mathematisch multiplizieren.
# "-" * 47 druckt das Minuszeichen exakt 47 Mal hintereinander auf den Bildschirm.
print("-" * 47)


# ------------------------------------------------------------------------------
# 3. VERSCHACHTELTE SCHLEIFEN (Das Herzstück der Tabelle)
# ------------------------------------------------------------------------------
# ÄUSSERE SCHLEIFE (Die Zeilen / Vertikal):
# Diese Schleife steuert die Reihen (Zeilen 1 bis 10) von oben nach unten.
for zeile in range(1, 11):
    # Am Anfang jeder Zeile drucken wir die aktuelle Zeilennummer (1 bis 10).
    # Wieder nutzen wir '{zeile:3}', um 3 Zeichen Platz zu reservieren,
    # gefolgt von dem vertikalen Trennstrich '|'.
    print(f"{zeile:3} |", end="")

    # INNERE SCHLEIFE (Die Spalten / Horizontal):
    # Für JEDE einzelne Zeile läuft diese Schleife komplett von 1 bis 10 durch.
    for spalte in range(1, 11):
        # Die eigentliche Mathematik: Zeile mal Spalte (z. B. 2 * 3 = 6).
        ergebnis = zeile * spalte

        # Wir drucken das Ergebnis.
        # {ergebnis:4} ist der wichtigste Trick hier: Es garantiert, dass eine
        # einstellige Zahl (wie 2) oder eine dreistellige (wie 100) immer exakt
        # den gleichen Platz (4 Zeichen) in der Tabelle einnimmt.
        # So entsteht die perfekte, gitterartige Struktur der Tabelle.
        print(f"{ergebnis:4}", end="")

    # Wenn die innere Schleife fertig ist (alle 10 Spalten einer Zeile gedruckt sind),
    # machen wir einen Zeilenumbruch, damit die nächste Zeile darunter beginnt.
    print()
