import pygame
import sys
import time

#variables de toma general 
ejecucion = True
frameRate = 60
frameCount = 0

#inicializacion de pygame
pygame.init()

#establecimiento del tamaño de pantalla
canvas = pygame.display.set_mode([600,400], pygame.RESIZABLE)

#funcion para la toma de eventos
def events():
    global ejecucion
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            ejecucion = False

#funcion de actualizacion de frames
def update():
    global frameCount
    
    events()
    
    pygame.display.flip()
    time.sleep(1/frameRate)
    
    frameCount += 1

#funcion de dibujo en el canvas
def draw():
    pygame.draw.rect(canvas, [frameCount % 255, 0,0], [0, 0, 600, 400])

#ciclo de repeticion durante ejecucion
while ejecucion:
    draw()
    update()
    
#cerrado de la pantalla 
sys.exit()