#Las transiciones dependen del número de células vecinas vivas:
#Una célula muerta con exactamente 3 células vecinas vivas "nace" (al turno siguiente estará viva).
#Una célula viva con 2 ó 3 células vecinas vivas sigue viva, en otro caso muere o permanece muerta (por "soledad" o "superpoblación").

import pygame
from random import randint
from collections import OrderedDict

# Definimos algunos colores
NEGRO = (0, 0, 0)
GRIS = (200, 200, 200)
BLANCO = (255, 255, 255)
VERDE = ( 0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 200)

# Establecemos el LARGO y ALTO de cada celda de la retícula.
LARGO = 10
ALTO = 10

# Establecemos el margen entre las celdas.
MARGEN = 1 

# Creamos un array bidimensional. Un array bidimensional
# no es más que una lista de listas.
grid = []
for fila in range(55):
    # Añadimos un array vacío que contendrá cada celda 
    # en esta fila
    grid.append([])
    for columna in range(90):
        grid[fila].append(0) # Añade una celda
        
# Creamos celulas vivas aleatoriamente 
for fila in range(55):
    for columna in range(90):
            if randint(0,5)==0:
                grid[fila][columna] = 1
        
# Inicializamos pygame
pygame.init()

# Establecemos el LARGO y ALTO de la pantalla
DIMENSION_VENTANA = [990, 605]
pantalla = pygame.display.set_mode(DIMENSION_VENTANA)

# Establecemos el título de la pantalla.
pygame.display.set_caption("Juego de la Vida")

# Iteramos hasta que el usuario pulse el botón de salir.
hecho = False
correr=False

# Lo usamos para establecer cuán rápido de refresca la pantalla.
reloj = pygame.time.Clock()

def LlenarRet():
    for fila in range(55):
        for columna in range(90):
            color = BLANCO
            if grid[fila][columna] == 1:
                color = AZUL                 
            pygame.draw.rect(pantalla,color,[(MARGEN+LARGO) * columna + MARGEN,(MARGEN+ALTO) * fila + MARGEN,LARGO,ALTO])
   

# -------- Bucle Principal del Programa----------
# -------- ----------- -------- -----------------
# -------- ----------- -------- -----------------
while not hecho:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            hecho = True
        if evento.type == pygame.MOUSEBUTTONDOWN:
            # El usuario presiona el ratón. Obtiene su posición.
            pos = pygame.mouse.get_pos()
            # Cambia las coordenadas x/y de la pantalla por coordenadas reticulares
            columna = pos[0] / (LARGO + MARGEN)
            fila = pos[1] / (ALTO + MARGEN)
            # Establece esa ubicación a cero
            grid[fila][columna] = 1
            print("Click ", pos, "Coordenadas de la retícula: ", fila, columna)
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                correr = not correr

    # Establecemos el fondo de pantalla.
    pantalla.fill(GRIS)

    # Dibujamos la retícula
    LlenarRet()
    
    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
    
    if correr:
        for fila in range(55):
            for columna in range(90):
                if grid[fila][columna] == 1:        
                    correr=False
                  
    # Limitamos a 20 fotogramas por segundo.
    reloj.tick(20)
    
# Pórtate bien con el IDLE.
pygame.quit()