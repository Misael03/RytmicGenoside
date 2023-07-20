#librerias
import pygame, sys
import random, math

#iniciando pygame
pygame.init()
clock = pygame.time.Clock()

#colores rgb
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

#ventana
size = [1000,700]
ventana = pygame.display.set_mode(size)

font1 = pygame.font.Font(None, 80)
font1.render("DarkTable", True, (255,0,0))
b , c , d = 0 , 0 , 0
a = 0
e = 1.5
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                sys.exit()
                pygame.quit()
    a += 0.018
    ventana.fill((b,c,d))
    b+=e
    c+=e
    d+=e
    if b > 254:
        e = 0
        ventana.blit(font1.render("DarkTable", True, (255,0,0)), ((size[0] / 2-120,size[1] / 2-65),(80,80)))
    if a > 5:
        run = False

    pygame.display.flip()
    clock.tick(60)