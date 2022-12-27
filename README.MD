![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709387-2b7ac180-571f-11eb-9b94-517aa6d501c9.png)


# Warsztat: Gra w zgadywanie liczb.

Napisz prostą grę w zgadywanie liczb. Komputer musi wylosować liczbę w zakresie 1 &ndash; 100. Następnie:

1. Zadać pytanie: "Guess the number: " i pobrać liczbę z klawiatury.
2. Sprawdzić, czy wprowadzony napis, to rzeczywiście liczba i w razie błędu wyświetlić komunikat "It's not a number!", 
po czym wrócić do pkt. 1
3. Jeśli liczba podana przez użytkownika jest mniejsza niż wylosowana, wyświetlić komunikat "To small!", 
po czym wrócić do pkt. 1.
4. Jeśli liczba podana przez użytkownika jest większa niż wylosowana, wyświetlić komunikat "To big!", 
po czym wrócić do pkt. 1.
5. Jeśli liczba podana przez użytkownika jest równa wylosowanej, wyświetlić komunikat "You win!", 
po czym zakończyć działanie programu.

##### Przykład:
```plaintext
Guess the number: cześć
It's not a number!
Guess the number: 50
To small!
Guess the number: 75
To big!
Guess the number: 63
You win!
```

> ## Pamiętaj, aby obsłużyć odpowiednie błędy! 

# Warsztat: Symulator LOTTO.

Jak zapewne wiesz, LOTTO to gra liczbowa polegająca na losowaniu 6 liczb z zakresu 1 &ndash; 49. 
Zadaniem gracza jest poprawne wytypowanie losowanych liczb. Nagradzane jest trafienie 3, 4, 5 lub 6 poprawnych liczb.

Napisz program, który:

1. zapyta o typowane liczby, przy okazji sprawdzi następujące warunki:
    * czy wprowadzony ciąg znaków jest poprawną liczbą,
    * czy użytkownik nie wpisał tej liczby już poprzednio,
    * czy liczba należy do zakresu 1-49,
2. po wprowadzeniu 6 liczb, posortuje je rosnąco i wyświetli na ekranie,
3. wylosuje 6 liczb z zakresu i wyświetli je na ekranie,
4. poinformuje gracza, ile liczb trafił.




# Warsztat: Gra w zgadywanie liczb 2 

Odwróćmy teraz sytuację z pierwszego zadania: ("Gra w zgadywanie liczb"). 
Niech użytkownik pomyśli sobie liczbę z zakresu 1-1000, a komputer będzie zgadywał. 
Zrobi to maksymalnie w 10 ruchach (pod warunkiem, że gracz nie będzie oszukiwał). 

Zadaniem gracza będzie udzielanie odpowiedzi "To small", "To big", "You win".

Do tego warsztatu dołączony jest schemat blokowy algorytmu. Zaimplementuj go w Pythonie.
![flowchart](images/flowchart.png)



# Warsztat: Gra w zgadywanie liczb 3

Zaimplementuj odwróconą grę w zgadywanie liczb w aplikacji webowej przy pomocy frameworka Flask.
Użytkownik dostaje do dyspozycji formularz z trzema guzikami: **To small**, **To big**, **You win**. 

Informacje o aktualnych zmiennych `min` i `max` przechowuj w ukrytych polach formularza (pole typu hidden).

> Uwaga &ndash; nie jest to rozwiązanie bezpieczne, bo użytkownik może ręcznie zmienić tego htmla, 
> np. przy pomocy Firebuga. W tej sytuacji jednak zupełnie wystarczające. Najwyżej zepsuje sobie zabawę ;)



# Warsztat: Kostka do gry

W grach planszowych i papierowych RPG używa się wielu rodzajów kostek do gry, nie tylko tych dobrze znanych, 
sześciennych. Jedną z popularniejszych kości jest np. kostka dziesięciościenna, a nawet stuścienna! 
Ponieważ w grach kośćmi rzuca się często, pisanie za każdym razem np. _"rzuć dwiema kostkami dziesięciościennymi, 
a do wyniku dodaj 20"_ byłoby nudne, trudne i marnowałoby ogromne ilości papieru. 
W takich sytuacjach używa się kodu _"rzuć 2D10+20"_. 

Kod takiej kostki wygląda następująco:

## xDy+z

gdzie:
* __y__ &ndash; rodzaj kostek, których należy użyć (np. D6, D10),
* __x__ &ndash; liczba rzutów kośćmi; jeśli rzucamy raz, ten parametr jest pomijalny,
* __z__ &ndash; liczba, którą należy dodać (lub odjąć) do wyniku rzutów (opcjonalnie).

__Przykłady:__

* __2D10+10__: 2 rzuty D10, do wyniku dodaj 10,
* __D6__: zwykły rzut kostką sześcienną,
* __2D3__: rzut dwiema kostkami trójściennymi,
* __D12-1__: rzut kością D12, od wyniku odejmij 1.

Napisz funkcję, która:

* przyjmie w parametrze taki kod w postaci łańcucha znaków, 
* rozpozna wszystkie dane wejściowe:
    * rodzaj kostki,
    * liczbę rzutów,
    * modyfikator,
* jeśli podany ciąg znaków jest niepoprawny, zwróci odpowiedni komunikat,    
* wykona symulację rzutów i zwróci wynik.

Typy kostek występujące w grach: D3, D4, D6, D8, D10, D12, D20, D100.   



# Warsztat: Salon gier (*)

Zaimplementuj grę 2001. Poniżej znajdziesz zasady.

## 2001 &ndash; Zasady Gry

1. Każdy z graczy zaczyna z liczbą punktów równą 0.
2. W swojej turze, gracz rzuca 2 kośćmi do gry (standardowe kości sześciościenne).
3. Wyrzucona liczba oczek jest dodawana do sumarycznej liczby punktów.
4. Począwszy od drugiej tury:
    * jeśli gracz wyrzuci 7, dzieli swoją liczbę punktów przez tę wartość odrzucając część ułamkową,
    * jeśli wyrzuci 11, mnoży aktualną liczbę punktów przez tę wartość.
5. Wygrywa gracz, który jako pierwszy uzyska 2001 punktów.


## Implementacja

* Zaimplementuj grę w wersji dla dwóch graczy. 
* Niech będzie to aplikacja konsolowa.
* Niech drugim graczem będzie komputer. 
* Po każdej turze wyświetl aktualną liczbę punktów.
* Rzut gracza, powinien odbywać się po naciśnięciu przez użytkownika klawisza enter. 
Rzut komputera następuje automatycznie, po rzucie gracza.
Zakończ program w momencie, gdy gracz, lub komputer osiągnie więcej niż 2001 punktów.


## Modyfikacja 1

Zauważyłeś pewno, że gra w obecnej wersji jest mało interaktywna i sprowadza się tylko i wyłącznie, do klikania
klawisza enter. Spróbujmy uczynić ją trochę bardziej interaktywną.

* Przed każdym rzutem, daj graczowi wybór. 
* Niech wybierze 2 kości z zestawu: D3, D4, D6, D8, D10, D12, D20, D100.
* Kości mogą się powtarzać, gracz może też użyć 2 różnych kości. 
* Niech wybór kości odbywa się za pomocą wprowadzenia odpowiedniego łańcucha znaków przez gracza
 (po jednym na każdą z kości). 
* Możesz wykorzystać kod z zadania **Kostka do gry**.
* Wybór kości przez komputer niech będzie losowy.

Reszta zasad pozostaje bez zmian. 


## Modyfikacja 2

Spróbuj teraz przenieść swoją grę na serwer przy użyciu Flaska. Aby przechowywać informację między turami, wykorzystaj
ukryte pola formularza. Nie jest to najlepsze rozwiązanie (może być podatne na oszukiwanie), 
ale na tę chwilę się tym nie przejmujemy. Wybór kości przed rzutem, powinien odbywać się za pomocą formularza.