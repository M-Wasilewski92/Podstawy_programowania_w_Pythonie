"""
Napisz prostą grę w zgadywanie liczb. Komputer musi wylosować liczbę w zakresie 1 – 100. Następnie:

Zadać pytanie: "Guess the number: " i pobrać liczbę z klawiatury.
1.Sprawdzić, czy wprowadzony napis, to rzeczywiście liczba i w razie błędu wyświetlić komunikat "It's not a number!", po
czym wrócić do pkt. 1
2.Jeśli liczba podana przez użytkownika jest mniejsza niż wylosowana, wyświetlić komunikat "To small!", po czym wrócić
do pkt. 1.
3.Jeśli liczba podana przez użytkownika jest większa niż wylosowana, wyświetlić komunikat "To big!", po czym wrócić do
pkt. 1.
4.Jeśli liczba podana przez użytkownika jest równa wylosowanej, wyświetlić komunikat "You win!", po czym zakończyć
 działanie programu.
"""

import random


def user_number():
    """Get number from user.
    
    Try until user give proper number.
    
    :rtype: int
    :return: give number as int 
    """

    while True:
        try:
            number = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number")
    return number


def finale_shuffle():
    """ shuffling function """
    correct_number = random.randint(1, 101)
    user_guess = user_number()

    while correct_number != user_guess:
        if correct_number < user_guess:
            print("To big!")
            user_guess = user_number()
        elif correct_number > user_guess:
            print("To small!")
            user_guess = user_number()
    else:
        print("You Win!")


if __name__ == '__main__':
    finale_shuffle()
