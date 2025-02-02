import numpy as np
import pygame as pg

# a szerokosc ekranu, b wysokosc
a=900
b=700
cellrozmiar=17
a_siatki=a//cellrozmiar
b_siatki=b//cellrozmiar
FPS=10

Kpola=(56, 56, 56)
Ksiatka=(112, 112, 112)
Kcell=(196, 22, 106)
K1=(0,0,0)z

pg.init()
ekran=pg.display.set_mode((a,b))
pg.display.set_caption("Game of life with player")
icon=pg.image.load("flower icon 1.png")
pg.display.set_icon(icon)
czas=pg.time.Clock()
siatka=np.zeros((b_siatki,a_siatki), dtype=int)

def lewomouse():
    if pg.mouse.get_pressed()[0]:
        q,w=pg.mouse.get_pos() #(q,w) = (x,y)
        qsiatka=q//cellrozmiar
        wsiatka=w//cellrozmiar
        if 0<=wsiatka and wsiatka<b_siatki and 0<=qsiatka and qsiatka<a_siatki:
            siatka[wsiatka,qsiatka]=1

def prawomouse():
    if pg.mouse.get_pressed()[2]:
        q,w=pg.mouse.get_pos()
        qsiatka=q//cellrozmiar
        wsiatka=w//cellrozmiar
        if 0<=wsiatka and wsiatka<b_siatki and 0<=qsiatka and qsiatka<a_siatki:
            plusglider(siatka,qsiatka,wsiatka)

def plusglider(siatka,x,y):
    glider=[(1,0),(2,1),(0,2),(1,2),(2,2)]
    for x1, y1 in glider:
        if 0<=x+x1<a_siatki and 0<=y+y1<b_siatki:
            siatka[y+y1,x+x1]=1
plusglider(siatka, 1,1)

running=True
time0=pg.time.get_ticks()
cellskolvo=np.sum(siatka)
while running:
    ekran.fill(Kpola)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
    lewomouse()
    prawomouse()
    for y in range(b_siatki):
        for x in range(a_siatki):
            rect=pg.Rect(x*cellrozmiar,y*cellrozmiar,cellrozmiar,cellrozmiar)
            if siatka[y,x]==1:
                pg.draw.rect(ekran,Kcell,rect)
            pg.draw.rect(ekran,Ksiatka,rect,1)
    nowasiatka=np.zeros((b_siatki,a_siatki), dtype=int)
    for y in range(b_siatki):
        for x in range(a_siatki):
            sasiad=siatka[max(0,y-1):min(b_siatki,y+2),max(0,x-1):min(a_siatki,x+2)]
            zyjesasiad=np.sum(sasiad) - siatka[y,x]
            if siatka[y,x]==1 and zyjesasiad in [2,3]:
                    nowasiatka[y,x]=1
            else:
                if siatka[y,x]==0 and zyjesasiad==3:
                    nowasiatka[y,x]=1
    siatka=nowasiatka

    cellskolvo=max(cellskolvo,np.sum(siatka))
    pg.display.flip()
    czas.tick(FPS)
bigtime=(pg.time.get_ticks()-time0)/1000
pg.quit()
print("czas gry = {:.02f} sekund".format(bigtime))
print("maks. liczba żywych komórek za czas gry = {}".format(cellskolvo))
