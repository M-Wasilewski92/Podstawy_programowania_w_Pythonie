"""
Jak zapewne wiesz, LOTTO to gra liczbowa polegająca na losowaniu 6 liczb z zakresu 1 – 49. Zadaniem gracza jest poprawne
wytypowanie losowanych liczb. Nagradzane jest trafienie 3, 4, 5 lub 6 poprawnych liczb.

Napisz program, który:

zapyta o typowane liczby, przy okazji sprawdzi następujące warunki:
czy wprowadzony ciąg znaków jest poprawną liczbą,
czy użytkownik nie wpisał tej liczby już poprzednio,
czy liczba należy do zakresu 1-49,
po wprowadzeniu 6 liczb, posortuje je rosnąco i wyświetli na ekranie,
wylosuje 6 liczb z zakresu i wyświetli je na ekranie,
poinformuje gracza, ile liczb trafił.
"""
import random


def user_hope():
    """Get six numbers from user.
    :rtype int
    :return: list of six numbers as int
    """
    while True:
        try:
            number = int(input("Podaj Liczbę "))
            break
        except ValueError:
            print("It's not a number")
    return number


def needed_numbers():
    """Get 6  numbers between 1 and 49.
    :rtype: list
    :return: list with 6 numbers provide by user
    """
    number_list = []
    while len(number_list) < 6:
        number = user_hope()
        if number not in number_list and 0 < number <= 49:
            number_list.append(number)
    return number_list


def sorted_print(numbers):
    """Print numbers in ascending order.

    :param list numbers: list of numbers
    :return:
    """
    print(", ".join([str(six_numbers) for six_numbers in sorted(numbers)]))


def wining_numbers():
    """Chose 6 random numbers

    :rtype: list
    :return: list with 6 random numbers
    """
    hope_crushers = list(range(1, 50))
    random.shuffle(hope_crushers)
    return hope_crushers[: 6]


def print_winner():
    """Main function"""
    user_numbers = needed_numbers()
    print("Your numbers: ")
    sorted_print(user_numbers)

    random_winners = wining_numbers()
    print("Lotto numbers:")
    sorted_print(random_winners)

    hits = 0
    for number in user_numbers:
        if number in random_winners:
            hits += 1

    print(f"You hit {hits} {'number' if hits == 1 else 'number'}!")


if __name__ == '__main__':
    print_winner()
