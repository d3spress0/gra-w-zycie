## Funkcji:
### 1. lewomouse()  
To funkcja, która dodaje żywą komórkę do pola w miejscu kliknięcia gdy gracz naciśnie na prawy przycisk myszy.  
*Wzór*:  
siatka[wsiatka,qsiatka]=1.  
*Argumenty*:  
funkcja nie posiada argumentów.  
*Wynik*:  
można zobaczyć, klikając prawym przyciskiem myszy, pojawienie nowej żywej komórki w miejscu nacisku.   
### 2. prawomouse()
To funkcja, która dodaje nowy glider do pola w miejscu kliknięcia gdy gracz naciśnie na lewy przycisk myszy.  
*Wzór*:  
plusglider(siatka,qsiatka,wsiatka).  
*Argumenty*:  
funkcja nie posiada argumentów.  
*Wynik*:  
można zobaczyć, klikając lewym przyciskiem myszy, pojawienie nowego glidera w miejscu nacisku.   
### 3. plusglider()
To funkcja, która tworzy nowy glider.  
*Wzór*:   
glider=[(1,0),(2,1),(0,2),(1,2),(2,2)], siatka[y+y1,x+x1]=1.  
*Argumenty*:  
siatka: dwuwymiarowa tablica, na której pojawie się glider. Każda komórka tablicy może mieć wartość 0 (martwa komórka) lub 1 (żywa komórka).
x, y: współrzędne komórki na tablice, w której zacznie się umieszczanie glidera.  
*Wynik*:  
stworzenie glidera, dla po dalszego wyświetlania.   