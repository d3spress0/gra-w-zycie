# gra-w-zycie
projekt na wstęp do programowania

Zasady gry w życie Conwaya:
Żywa komórka z mniej niż dwoma żywymi sąsiadami umiera (samotność).

Żywa komórka z dwoma lub trzema żywymi sąsiadami pozostaje żywa (przetrwanie).

Żywa komórka z więcej niż trzema żywymi sąsiadami umiera (przeludnienie).

Martwa komórka z dokładnie trzema żywymi sąsiadami staje się żywa (reprodukcja).


Przykład kodu DO SPRAWDZENIA PRZEZ NASTKĘ Z JEJ KODEM

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Rozmiar planszy
N = 100

# Funkcja tworząca początkowy układ
def initial_state(N):
    return np.random.choice([0, 1], size=(N, N))

# Funkcja aktualizująca planszę
def update(frameNum, img, grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# Main code
ON = 255
OFF = 0
vals = [ON, OFF]

grid = initial_state(N)

fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                              frames=10,
                              interval=50,
                              save_count=50)

plt.show()
