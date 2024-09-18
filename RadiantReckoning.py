
import pygame
from CharacterObject import Character
pygame.init()


#creates game screen and caption
screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
pygame.display.set_caption("Radiant Reckoning")

gameover = False
clock = pygame.time.Clock()
joseph = Character(135, 276, "joseph", "sample", 20, 5, 5)

#BEGIN GAME LOOP######################################################
while not gameover:  # GAME LOOP############################################################
    ticks = clock.get_time()
    clock.tick(60)  # FPS
    gameEvents = pygame.event.get()
    # Input Section------------------------------------------------------------
    for event in gameEvents:  # quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
    #keyboard input-----------------------------------
  

    joseph.move()
     
    #render section-----------------------------------vis
    screen.fill((0,0,0))


    joseph.draw(screen)


    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()
