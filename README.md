# gra-w-zycie
projekt na wstęp do programowania

Zasady gry w życie Conwaya:
Żywa komórka z mniej niż dwoma żywymi sąsiadami umiera (samotność).

Żywa komórka z dwoma lub trzema żywymi sąsiadami pozostaje żywa (przetrwanie).

Żywa komórka z więcej niż trzema żywymi sąsiadami umiera (przeludnienie).

Martwa komórka z dokładnie trzema żywymi sąsiadami staje się żywa (reprodukcja).


Przegląd kodu
Importowanie bibliotek:

numpy (alias np) jest używany do operacji na tablicach i macierzach.

pygame (alias pg) jest używany do tworzenia okienka graficznego i interakcji.

Ustawienia początkowe:

Definicja szerokości (a) i wysokości (b) ekranu.

Rozmiar pojedynczej komórki (cellrozmiar).

Liczba komórek na siatce w pionie (a_siatki) i poziomie (b_siatki).

Ustawienie liczby klatek na sekundę (FPS).

Kolory:

Kolory tła, siatki, komórek i inne są zdefiniowane w formacie RGB.

Inicjalizacja pygame:

Tworzenie okna gry i ustawianie ikonki oraz tytułu okna.

Siatka:

Tablica siatka jest inicjalizowana zerami, co oznacza, że na początku wszystkie komórki są martwe.

Funkcja lewomouse:

Obsługuje naciśnięcie lewego przycisku myszy i zmienia stan komórek na żywe w miejscu, gdzie kliknięto.

Główna pętla gry (while running):

Odświeża ekran, obsługuje zdarzenia (np. zamknięcie okna).

Rysuje komórki na ekranie.

Aktualizuje stan każdej komórki na podstawie liczby żywych sąsiadów zgodnie z zasadami gry w życie Conwaya.

Autorzy projektu:
- Natalia Gała
- Anastasiia Khomenko
- Zuzanna Seniuk
