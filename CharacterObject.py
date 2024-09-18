from GameObject import GameObject
import pygame

class Character(GameObject):
    def __init__(self, xpos, ypos, name, description, health, damage, defense, level=1, experience=0):
        super().__init__(xpos, ypos, name, description, "character", health, damage, defense)
        self.level = level
        self.experience = experience
        self.pos = pygame.Vector2(xpos, ypos)
        self.velocity = pygame.Vector2(0, 0)

    def move(self, speed = 10):
        keys = pygame.key.get_pressed()
        self.velocity.x = speed if keys[pygame.K_RIGHT] or keys[pygame.K_d] else -speed if keys[pygame.K_LEFT] or keys[pygame.K_a] else 0
        self.velocity.y = speed if keys[pygame.K_DOWN] or keys[pygame.K_s] else -speed if keys[pygame.K_UP] or keys[pygame.K_w] else 0
        self.pos += self.velocity

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 255), (self.pos.x, self.pos.y, 20, 20)) 