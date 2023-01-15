# gra kolko i krzyzyk - komputer rozpoczyna grę - komputer jest krzyżykiem - użytkownik jest kolkiem
# Tworzymy szablon
szablon = " {} {} {}\n {} {} {}\n {} {} {}"
# deklarujemy wartości początkowe pól
p1 = '-'
p2 = '-'
p3 = '-'
p4 = '-'
p5 = 'X'
p6 = '-'
p7 = '-'
p8 = '-'
p9 = '-'
kontrolna = 1
# poczatek programu wyswietlamy plansze
komunikat = szablon.format(p1, p2, p3, p4, p5, p6, p7, p8, p9)
print(komunikat)
# Pobieramy identyfikator pola od użytkownika
while p1 == '-' or p2 == '-' or p3 == '-' or p4 == '-' or p5 == '-' or p6 == '-' or p7 == '-' or p8 == '-' or p9 == '-':
    px = input("Podaj identyfikator pola: ")
    while str(px) not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        print("Błąd!!  Podaj liczbę całkowitą z zakresu 1 - 9")
        px = '-'
        kontrolna = 0
        px = input("Podaj identyfikator pola: ")
    px = "p" + px
# weryfikujemy zajestosc pola i jesli wolne wpisujemy ruch gracza
    if str(px) == "p1":
        if p1 != '-':
            print("Błąd - pole zajęte")
            kontrolna = 0
        else:
            p1 = 'O'
    elif str(px) == "p2":
        if p2 != '-':
            print("Błąd - pole zajęte")
            kontrolna = 0
        else:
            p2 = 'O'
    elif str(px) == "p3":
        if p3 != '-':
            print("Błąd - pole zajęte")
            kontrolna = 0
        else:
            p3 = 'O'
    elif str(px) == "p4":
        if p4 != '-':
            print("Błąd - pole zajęte")
            kontrolna = 0
        else:
            p4 = 'O'
    elif str(px) == "p5":
        if p5 != '-':
            print("Błąd - pole zajęte")
            kontrolna = 0
        else:
            p5 = 'O'
    elif str(px) == "p6":
        if p6 != '-':
            print("Błąd - pole zajęte")
            kontrolna = 0
        else:
            p6 = 'O'
    elif str(px) == "p7":
        if p7 != '-':
            print("Błąd - pole zajęte")
            kontrolna = 0
        else:
            p7 = 'O'
    elif str(px) == "p8":
        if p8 != '-':
            print("Błąd - pole zajęte")
            kontrolna = 0
        else:
            p8 = 'O'
    elif str(px) == "p9":
        if p9 != '-':
            print("Błąd - pole zajęte")
            kontrolna = 0
        else:
            p9 = 'O'
# komputer wykonuje ruch - ew można bardziej rozbudować
    if kontrolna == 1:
        if p2 == '-':
            p2 = 'X'
        elif p4 == '-':
            p4 = 'X'
        elif p6 == '-':
            p6 = 'X'
        elif p8 == '-':
            p8 = 'X'
        elif p3 == '-':
            p3 = 'X'
        elif p7 == '-':
            p7 = 'X'
        elif p1 == '-':
            p1 = 'X'
        elif p9 == '-':
            p9 = 'X'
    kontrolna = 1
    komunikat = szablon.format(p1, p2, p3, p4, p5, p6, p7, p8, p9)
    print(komunikat)
# oceniamy i ew konczymy gre
    if ((p1 == 'X' and p4 == 'X' and p7 == 'X') or (p1 == 'X' and p2 == 'X' and p3 == 'X')
        or (p3 == 'X' and p6 == 'X' and p9 == 'X') or (p7 == 'X' and p8 == 'X' and p9 == 'X')
        or (p1 == 'X' and p5 == 'X' and p9 == 'X') or (p3 == 'X' and p5 == 'X' and p7 == 'X')
        or (p2 == 'X' and p5 == 'X' and p8 == 'X') or (p4 == 'X' and p5 == 'X' and p6 == 'X')
        ) and ((p1 == 'O' and p4 == 'O' and p7 == 'O') or (p1 == 'O' and p2 == 'O' and p3 == 'O')
        or (p3 == 'O' and p6 == 'O' and p9 == 'O') or (p7 == 'O' and p8 == 'O' and p9 == 'O')
        or (p1 == 'O' and p5 == 'O' and p9 == 'O') or (p3 == 'O' and p5 == 'O' and p7 == 'O')
        or (p2 == 'O' and p5 == 'O' and p8 == 'O') or (p4 == 'O' and p5 == 'O' and p6 == 'O')):
        print("Remis")
        break
    elif ((p1 == 'O' and p4 == 'O' and p7 == 'O') or (p1 == 'O' and p2 == 'O' and p3 == 'O')
        or (p3 == 'O' and p6 == 'O' and p9 == 'O') or (p7 == 'O' and p8 == 'O' and p9 == 'O')
        or (p1 == 'O' and p5 == 'O' and p9 == 'O') or (p3 == 'O' and p5 == 'O' and p7 == 'O')
        or (p2 == 'O' and p5 == 'O' and p8 == 'O') or (p4 == 'O' and p5 == 'O' and p6 == 'O')):
        print("Wygrana")
        break
    elif ((p1 == 'X' and p4 == 'X' and p7 == 'X') or (p1 == 'X' and p2 == 'X' and p3 == 'X')
        or (p3 == 'X' and p6 == 'X' and p9 == 'X') or (p7 == 'X' and p8 == 'X' and p9 == 'X')
        or (p1 == 'X' and p5 == 'X' and p9 == 'X') or (p3 == 'X' and p5 == 'X' and p7 == 'X')
        or (p2 == 'X' and p5 == 'X' and p8 == 'X') or (p4 == 'X' and p5 == 'X' and p6 == 'X')):
        print("Przegrana")
        break
# print(komunikat)
