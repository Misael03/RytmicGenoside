#librerias
import pygame, sys
import random, math
import data.engine as e
try:
    import starting.py
except:
#iniciando pygame
    pygame.init()
    clock = pygame.time.Clock()

    #colores rgb
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    white = (255,255,255)
    black = (0,0,0)
    e.set_global_colorkey(black)

    #imagenes
    arbol1 = pygame.image.load("arbol1.png")
    arbol1.set_colorkey(white)

    #ventana
    size = (1000,700)
    ventana = pygame.display.set_mode(size,0,32)
    display = pygame.Surface((size[0]/4, size[1]/4))

    #fuentes
    font1 = pygame.font.Font(None, 20)
    font2 = pygame.font.Font(None, 40)
    font3 = pygame.font.Font(None, 80)
    
    #stats
    coins = 0
    
    #cargando animaciones
    e.load_animations("data/entidades/")
    
    #jugador
    player = e.entity(100,100, 12,23,"player")
    moving_right = False
    moving_left = False
    moving_down = False
    moving_top = False
    
    #arboles
    arboles = []
    for i in range (20):
        arboles.append((arbol1, random.randrange(40,960), random.randrange(40,660), 12, 27))
    
    true_scroll = [0,0]
    run = True
    x, y = 500/2, 350/2
    while run:
        display.fill((146,244,255))
        #adquiriendo x e y coordenas del mosuse
        x, y = pygame.mouse.get_pos()
        #configurando zoom de la pantalla
        true_scroll[0] += (player.x-true_scroll[0]-(125-player.size_x/2))/20
        true_scroll[1] += (player.y-true_scroll[1]-(87.5-player.size_y/2))/20
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])
        tile_rects = []
        #configurando jugador
        player_movement = [0,0]
        if moving_right == True:
            player_movement[0] += 1
        if moving_left == True:
            player_movement[0] -= 1
        if moving_down == True:
            player_movement[1] += 1
        if moving_top == True:
            player_movement[1] -= 1
        
        if player_movement[0] == 0:
            player.set_action('idle')
        if player_movement[0] > 0:
            player.set_flip(False)
            player.set_action('run')
        if player_movement[0] < 0:
            player.set_flip(True)
            player.set_action('run')
        display.blit(font1.render(f"monedas: {coins}", True, black), ((10,10),(60,10)))
        for arbol in arboles:
            display.blit(arbol[0],((arbol[1]-scroll[0], arbol[2]-scroll[1]), (arbol[3], arbol[4])))
            tile_rects.append(pygame.Rect(arbol[1]-scroll[0],arbol[2]-scroll[1],arbol[3],arbol[4]))
            #pygame.draw.rect(display, red, ((arbol[1], arbol[2]),(arbol[3], arbol[4])))
        pygame.draw.rect(display,blue,((player.x,player.y),(player.size_x,player.size_y)))
        
        player.move(player_movement,tile_rects)
        player.change_frame(1)
        player.display(display,scroll)
        ventana.blit(pygame.transform.scale(display,size),(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_TAB:
                    print(x,y)
                    print(player.action, player.image)
                    print(player.x,player.y)
                if event.key == pygame.K_LEFT:
                    moving_left = True
                if event.key == pygame.K_RIGHT:
                    moving_right = True
                if event.key == pygame.K_DOWN:
                    moving_down = True
                if event.key == pygame.K_UP:
                    moving_top = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    moving_left = False
                if event.key == pygame.K_RIGHT:
                    moving_right = False
                if event.key == pygame.K_DOWN:
                    moving_down = False
                if event.key == pygame.K_UP:
                    moving_top = False
        pygame.display.update()
        clock.tick(60)