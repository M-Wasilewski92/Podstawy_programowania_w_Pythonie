"""
Odwróćmy teraz sytuację z pierwszego zadania: ("Gra w zgadywanie liczb"). Niech użytkownik pomyśli sobie liczbę z zakresu 1-1000, a komputer będzie zgadywał. Zrobi to maksymalnie w 10 ruchach (pod warunkiem, że gracz nie będzie oszukiwał).

Zadaniem gracza będzie udzielanie odpowiedzi "To small", "To big", "You win".

Do tego warsztatu dołączony jest schemat blokowy algorytmu. Zaimplementuj go w Pythonie.

"""


def secret_number():
    """Pick number between 0 and 1000
    :rtype: int
    :return: number from user
    """
    while True:
        try:
            number = int((input("Pomyśl liczbę od 0 do 1000 a ja ją zgadnę w max. 10 próbach: ")))

        except ValueError:
            print("To nie jest nawet liczba!")
            continue
        if 0 <= number <= 1000:
            return number
        else:
            print("To nie jest liczba z przedziału 1-1000!")
            return number


def gueess():
    caunter = 0

    minimal_val = 0
    maximal_val = 1000
    while caunter <= 10:
        guess = ((maximal_val - minimal_val) // 2 + minimal_val)
        print(f"Zgaduję: {guess}!")
        if input("y/n") == "y":
            return print("Wygrałem!")
        else:
            temp = input("+ = za dużo?, - = za mało?")
            if temp == "-":
                minimal_val = guess
                caunter += 1
            elif temp == "+":
                maximal_val = guess
                caunter += 1
            else:
                return "Nie oszukuj"


print(secret_number())
print(gueess())
