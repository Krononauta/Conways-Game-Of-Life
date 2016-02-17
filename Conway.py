"""
 Programa de ejemplo de c�mo usar un array para respaldar una ret�cula en pantalla.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

V�deo explicativo: http://youtu.be/mdTeqiWyFnc
"""
import pygame

# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = ( 0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# Establecemos el LARGO y ALTO de cada celda de la ret�cula.
LARGO  = 20
ALTO = 20

# Establecemos el margen entre las celdas.
MARGEN = 5

# Creamos un array bidimensional. Un array bidimensional
# no es m�s que una lista de listas.
grid = []
for fila in range(10):
    # A�adimos un array vac�o que contendr� cada celda 
    # en esta fila
    grid.append([])
    for columna in range(10):
        grid[fila].append(0) # A�ade una celda

# Establecemos la fila 1, celda 5 a uno. (Recuerda, los n�meros de las filas y
# columnas empiezan en cero.)
grid[1][5] = 1
grid[3][3] = 1

# Inicializamos pygame
pygame.init()

# Establecemos el LARGO y ALTO de la pantalla
DIMENSION_VENTANA = [255, 255]
pantalla = pygame.display.set_mode(DIMENSION_VENTANA)

# Establecemos el t�tulo de la pantalla.
pygame.display.set_caption("Ret�culas y Matrices")

# Iteramos hasta que el usuario pulse el bot�n de salir.
hecho = False

# Lo usamos para establecer cu�n r�pido de refresca la pantalla.
reloj = pygame.time.Clock()

# -------- Bucle Principal del Programa-----------
while not hecho:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            hecho = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # El usuario presiona el rat�n. Obtiene su posici�n.
            pos = pygame.mouse.get_pos()
            # Cambia las coordenadas x/y de la pantalla por coordenadas reticulares
            columna = pos[0] / (LARGO + MARGEN)
            fila = pos[1] / (ALTO + MARGEN)
            # Establece esa ubicaci�n a cero
            grid[fila][columna] = 1
            print("Click ", pos, "Coordenadas de la ret�cula: ", fila, columna)

    # Establecemos el fondo de pantalla.
    pantalla.fill(NEGRO)

    # Dibujamos la ret�cula
    for fila in range(10):
        for columna in range(10):
            color = BLANCO
            if grid[fila][columna] == 1 and fila==3:
                color = AZUL            
            if grid[fila][columna] == 1 and color!=AZUL:
                color = VERDE
            
            pygame.draw.rect(pantalla,color,[(MARGEN+LARGO) * columna + MARGEN,(MARGEN+ALTO) * fila + MARGEN,LARGO,ALTO])

    # Limitamos a 20 fotogramas por segundo.
    reloj.tick(20)

    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

# P�rtate bien con el IDLE.
pygame.quit()