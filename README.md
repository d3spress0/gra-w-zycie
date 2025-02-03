# Project "Gra w zycie"
### Temat projektu
Gra w zycie (The game of life) - automat komórkowy Johna Conwaya.
### Zasady gry
1. Martwa komórka, która ma dokładnie 3 żywych sąsiadów, staje się żywa w następnej jednostce czasu (rodzi się)  
2. Żywa komórka z 2 albo 3 żywymi sąsiadami pozostaje nadal żywa; przy innej liczbie sąsiadów umiera (z „samotności” albo „zatłoczenia”)
### Jak dziala nasz projekt?
Nasz projekt "Gra w życie" jest zrobiony tak, żeby w niego dało się grac. Wiec po uruchomieniu kodu, przed graczem odpala się szare pole podzielone na komórki, które są martwi oraz "idąca" przez pole figura, nazywająca się glider. Gracz ma funkcji dodawania nowych komórek oraz nowych gliderow, które przy dotykaniu się mogą stworzyć nowe ciekawe kombinacji. Gra skończy się, aż gracz zachce tego, wtedy powinien nacisnąć na krzyżyk albo na Esc. Po zakryciu program na dole wypisze graczowi, ile czasu on grał oraz największą liczbę żywych komórek na polu za cały czas grania.
### Używane biblioteki
1. numpy (alias np) jest używany do operacji na tablicach i macierzach.
2. pygame (alias pg) jest używany do tworzenia okienka graficznego i interakcji.
### Ustawienia początkowe:
1. Definicja szerokości (a) i wysokości (b) ekranu.
2. Rozmiar pojedynczej komórki (cellrozmiar).
3. Liczba komórek na siatce w pionie (a_siatki) i poziomie (b_siatki).
4. Ustawienie liczby klatek na sekundę (FPS).
### Autorzy projektu:
Natalia Gała  
Anastasiia Khomenko  
Zuzanna Seniuk  
