from datetime import date
import inflect
import sys

def main():
    birth = input("date of birth, YYYY-MM-DD: ")
    if not fecha_correcta(birth):
        print("Invalid date format")
        sys.exit(1)
    
    try:
        result = calc_age(birth)
        print(result)
    except ValueError:
        print("Algo está mal. Por favor use una fecha válida.")
        sys.exit(1)

def fecha_correcta(birth):
    parts = birth.split("-")
    if len(parts) != 3:
        return False
    y, m, d = parts
    return len(y) == 4 and y.isdigit() and m.isdigit() and d.isdigit()

def calc_age(birth):
    try:
        parts = birth.split("-")
        y, m, d = parts
        b_day = date(int(y), int(m), int(d))
        today = date.today()
        diferencia = today - b_day
        min_number = diferencia.days * 1440
        min_w = inflect.engine()
        words = min_w.number_to_words(min_number, andword="")
        return f"{words.capitalize()} minutes"
    except ValueError:
        raise ValueError("Algo está mal. Por favor use una fecha válida.")

if __name__ == "__main__":
    main()
