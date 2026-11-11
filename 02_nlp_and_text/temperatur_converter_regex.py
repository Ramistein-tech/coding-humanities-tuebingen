# pylint: disable = c0103, w0311
"========== Temperatur umrechnen =========="

# Module nachladen
import re

# Benutzereingabe für die Temperatur, bis ein gültiger Wert eingegeben wurde
while True:
    temp = input(
        "Bitte geben Sie die Temperatur in Celsius (°C), Fahrenheit (°F) oder Kelvin (K) ein: "
    )
    # Angenäherte Lösung zur Validierung der Eingabe
    # if temp.endswith('K') or temp.endswith('°C') or temp.endswith('°F'):
    # Sicherstellen, daß die Eingabe dem Muster Zahl + Einheit entspricht
    if re.match(r"^\d+([.,]\d+)?\s?K$|^-?\d+([.,]\d+)?\s?(°C|°F)$", temp):
        break  # Beendet die While-Schleife
    # Fehlermeldung bei ungültiger Eingabe
    print(
        "Ungültige Eingabe. Bitte geben Sie die Temperatur als eine Zahl"
        " mit Einheit (°C, °F , K) ein. Kelvin kennt keine Werte unter 0."
    )

# Zerlegung der Eingabe in Zahlenwert und Einheit mit Bedingung
value = (
    temp[:-1].replace(",", ".") if temp.endswith("K") else temp[:-2].replace(",", ".")
)
unit = temp[-1:] if temp.endswith("K") else temp[-2:]
# Validierung der Zahl
value = float(value)

# Umrechnungen basierend auf der Einheit
match unit.upper():
    case "°F":
        # Umrechnung von Fahrenheit in Celsius und Kelvin
        temp_out1 = round((value - 32) * 5 / 9, 2)
        temp_out2 = round(temp_out1 + 273.15, 2)
        # Umwandlung in String und setzen der Einheit
        temp_out1 = str(temp_out1) + " °C"
        temp_out2 = str(temp_out2) + " K"
    case "K":
        # Umrechnung von Kelvin in Celsius und Fahrenheit
        temp_out1 = round(value - 273.15, 2)
        temp_out2 = round((temp_out1 * 9 / 5) + 32, 2)
        # Umwandlung in String und setzen der Einheit
        temp_out1 = str(temp_out1) + " °C"
        temp_out2 = str(temp_out2) + " °F"
    case "°C":
        # Umrechnung von Celsius in Fahrenheit und Kelvin
        temp_out1 = round((value * 9 / 5) + 32, 2)
        temp_out2 = round(value + 273.15, 2)
        # Umwandlung in String und setzen der Einheit
        temp_out1 = str(temp_out1) + " °F"
        temp_out2 = str(temp_out2) + " K"

# Komma als Dezimaltrennzeichen setzen
temp_out1 = temp_out1.replace(".", ",")
temp_out2 = temp_out2.replace(".", ",")
# Ausgabe der umgerechneten Temperatur
print(
    f"\nDie eingegebene Temperatur beträgt {temp_out1} oder {temp_out2}.", end="\n" * 2
)
