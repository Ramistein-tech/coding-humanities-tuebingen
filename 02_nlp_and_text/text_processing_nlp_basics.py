# pylint: disable = C0103
# ========== Strings manipulieren ==========

x = chr(67)
n = ord('d')
print(x, n, sep='\t')

satz = 'wenn Fliegen hinter Fliegen fliegen, fliegen Fliegen Fliegen nach.'
print(satz, end='\n'*2)

# Teilstrings (Slicing)
print(satz[5:])
print(satz[5:12])
print(satz[:36])
print(satz[-5:-1], end='\n'*2)

# Stringslänge messen
print(f'Die Länge des Satzes beträgt {len(satz)} Zeichen.')

# Vorkommen zählen (Frequenzanalyse)
# Anführungszeichen innerhalb des f-Strings korrigiert
print(f'Das Verb "fliegen" im Satz: {satz.count("fliegen")}')
print(f'Das Sub "Fliegen" im Satz: {satz.count("Fliegen")}')

# Finden von Teilstrings
posHinter = satz.find('hinter')
posFliegen1 = satz.find('Fliegen')
posFliegen2 = satz.rfind('Fliegen')

print(f'Die Position von "hinter" im Satz: {posHinter}', end='\n\n')
print(f'Die Position von "Fliegen" im Satz: {posFliegen1}')
print(f'Die Position von "Fliegen" (von rechts) im Satz: {posFliegen2}', end='\n\n')
print(f'Das erste Wort "Fliegen" beginnt bei: {satz.index("Fliegen")}', end='\n\n')

# Zerlegen eines Strings in Wörter (Tokenisierung)
elemente = satz.split(' ')  # Typo 'spilt' behoben
print(elemente)
print(f'Anzahl der Wörter im Satz: {len(elemente)}')

# Interpunktion entfernen (Zuordnungstabelle)
translate_strings = str.maketrans('', '', ',.')
woerter = satz.translate(translate_strings).split(' ')
print(woerter)
print(f'Anzahl der bereinigten Wörter im Satz: {len(woerter)}', end='\n\n')

# Trennzeichen mit der Liste von Strings verbinden (Konkatenation)
neuer_satz1 = ' '.join(elemente)
neuer_satz2 = ' '.join(woerter)
print(neuer_satz1, neuer_satz2, sep='\n'*2)

# Merkwürdige Strings (Whitespace-Eliminierung & Shadowing behoben)
# Variable 'str' umbenannt, um das Python-Built-in nicht zu verdecken
str_val = '  \n\t Hello, \t World!  \n  '
print(f'Originaler String: "{str_val}"')
print(f'Bereinigter String: "{str_val.strip()}"', end='\n\n')
 
# Coloured adjectives in a "lousy" text (Multiline-Strings verwenden)
text = """Python is a high-level, general-purpose programming language that emphasizes code readability, simplicity, and ease-of-writing with the use of significant indentation,
an extensive ("batteries-included") standard library, and garbage collection. Python supports multiple programming paradigms but with an emphasis on object-oriented programming and dynamic typing.
Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language.
Python 3.0, released in 2008, was a major revision and not completely backward-compatible with earlier versions.
Beginning with Python 3.5, capabilities and keywords for typing were added to the language, allowing optional static typing.
As of 2026, the Python Software Foundation supports Python 3.11, 3.12, 3.13, 3.14, and 3.15, following the project's annual release cycle and five-year support policy.
Python 3.15.0 the latest stable version defaults to UTF-8, unlike previous versions. Earlier versions in the 3.x series have reached end-of-life and no longer receive security updates."""

print(text)