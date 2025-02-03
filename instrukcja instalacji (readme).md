## Instrukcja obsługi projektu Gra w życie  
### 1. Pobierz repozytorium [tutaj](https://github.com/d3spress0/gra-w-zycie.git)  
1) rozpakuj plik gra-w-zycie-main.zip  
2) otwórz Git Bash, Git CMD lub CMD(terminal)  

### 2. Stwórz środowisko myenv w Git Bashu, Git CMD lub CMD(terminal):  
1) wpisz `cd C:\sziezka\do\rozpakowanego\pliku\gra-w-zycie-main.zip`   
2) dalej wpisz `python -m venv myenv`   
3) dalej wpisz `myenv\Scripts\activate` (na systemie Windows) lub `source myenv/bin/activate` (na systemie Unix albo MacOS)  

### 3. Instalowanie dodatkowych bibliotek (numpy i pygame) w Git Bashu, Git CMD lub CMD(terminal):  
1) wpisz `pip install -r requirements.txt`  

### 3. Uruchomienie gry w Git Bashu, Git CMD lub CMD(terminal):  
1) wpisz `python gameoflife.py`  
2) graj w grę, mając trzy funkcji do wybory:  
   1. dodać nową żyjącą komórkę na polu, naciskając lewy przycisk myszy   
   2. dodać nową żyjącą figurę (glider) na polu, naciskając prawy przycisk myszy  
   3. wyjść z gry, naciskając na krzyżyk lub Esc  
3) zobacz wyniki gry, napisane w programie, w którym uruchomiałeś/aś kod (Git Bash, Git CMD lub CMD(terminal)), po wyjściu z gry. Wyniki:  
   1. czas grania gracza  
   2. największa liczba żywych komórek na polu za cały czas grania  
