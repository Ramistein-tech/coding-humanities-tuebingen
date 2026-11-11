"""
Control Flow and Interactive Age Calculation.

Demonstrates user input parsing, dynamic date extraction using datetime,
and exception handling for robust CLI applications.
"""

from datetime import datetime


def calculate_age() -> None:
    """Calculates user age based on current year with input validation."""
    current_year: int = datetime.now().year

    try:
        birth_year_input = input("In welchem Jahr wurdest du geboren? ")
        birth_year: int = int(birth_year_input.strip())

        # Validation bounds check (die Bereichsprüfung)
        if birth_year > current_year or birth_year < 1900:
            print(f"Fehler: Ungültiges Geburtsjahr (1900 - {current_year}).")
            return

        age: int = current_year - birth_year
        print(f"Du bist vermutlich {age - 1} oder {age} Jahre alt.")

    except ValueError:
        print("Fehler: Bitte geben Sie eine gültige Jahreszahl ein.")


if __name__ == "__main__":
    calculate_age()
