"""
Interactive CLI Temperature Converter with Delimiter Separation.
"""


def temperatur_konverter() -> None:
    while True:
        eingabe = (
            input("\nTemperatur eingeben (z. B. 25 C) oder ENDE tippen: ")
            .strip()
            .upper()
        )

        if eingabe == "ENDE":
            print("Das Programm wird beendet.")
            break

        if " " not in eingabe:
            print("Fehler: Bitte ein Leerzeichen zwischen Zahl und Einheit setzen.")
            continue

        zahl_str, einheit = eingabe.split(" ", 1)

        try:
            # معالجة الفاصلة العشرية الألمانية قبل التحويل
            zahl = float(zahl_str.replace(",", "."))
        except ValueError:
            print("Fehler: Der eingegebene Wert ist keine gültige Zahl.")
            continue

        match einheit:
            case "C":
                f = (zahl * 9 / 5) + 32
                print(f"Ergebnis: {f:.2f} °F")
            case "F":
                c = (zahl - 32) * 5 / 9
                print(f"Ergebnis: {c:.2f} °C")
            case _:
                print("Fehler: Unbekannte Maßeinheit. Bitte C oder F verwenden.")


if __name__ == "__main__":
    temperatur_konverter()
