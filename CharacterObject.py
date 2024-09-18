from GameObject import GameObject
import pygame

class Character(GameObject):
    def __init__(self, xpos, ypos, name, description, health, damage, defense, level=1, experience=0):
        super().__init__(xpos, ypos, name, description, "character", health, damage, defense)
        self.level = level
        self.experience = experience 

    def move(self, gameEvents, speed = 10):

        keys = pygame.key.get_pressed()
        for event in gameEvents:  # quit game if x is pressed in top corner
            if event.type == pygame.KEYDOWN:  # keyboard input
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    self.xpos -= speed
                elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    self.xpos += speed
                elif keys[pygame.K_RIGHT] or keys[pygame.K_w]:
                    self.ypos -= speed
                elif keys[pygame.K_RIGHT] or keys[pygame.K_s]:
                    self.ypos += speed











    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 255), (self.xpos, self.ypos, 20, 20)) 