import pygame as pg
import random
import time

class Tahm:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 75
        self.height = 75
        self.image = pg.image.load("tahm.png") 
        self.image = pg.transform.scale(self.image, (self.width, self.height)) 
        self.rect = self.image.get_rect()  
        self.health = 5
        self.health_image = pg.image.load("hjerte.png")
        self.health_image = pg.transform.scale(self.health_image, (50, 50))
        self.health_loss_delay = 10 # added delay variable
        
    def update(self, player_direction, game_map, monsters):
        new_x, new_y = self.x, self.y
        if player_direction == "left":
            new_x -= 10
        elif player_direction == "right":
            new_x += 10
        elif player_direction == "up":
            new_y -= 10
        elif player_direction == "down":
            new_y += 10

        # Check for kant kollision
        if new_x < 0 or new_x + self.width > game_map.get_width():
            return
        if new_y < 0 or new_y + self.height > game_map.get_height():
            return

        # Check for kollision with game map
        for i in range(new_x, new_x + self.width):
            for j in range(new_y, new_y + self.height):
                if game_map.get_at((i, j)) == (0, 0, 0, 255):
                    return  # stop bevælgelse

        # Check for collision with monsters
        for monster in monsters:
            if self.rect.colliderect(monster.rect) and self.health_loss_delay == 0:
                self.health -= 1
                self.health_loss_delay = 20 # set delay before another health loss can occur
        
        # Reduce the health loss delay counter
        if self.health_loss_delay > 0:
            self.health_loss_delay -= 1

        # hvis ingen collision detected
        self.x, self.y = new_x, new_y
        self.rect.x, self.rect.y = self.x, self.y 
        
    def draw(self, screen):
        # Calculate the starting x-coordinate for the health images
        health_x = (screen.get_width() - self.health * 50) / 2
        
        # Draw the main image
        screen.blit(self.image, self.rect)
        
        # Draw the health images
        for i in range(self.health):
            screen.blit(self.health_image, (health_x + i * 50, 0))

class Monster:
    def __init__(self, x, y, tahm):
        self.tahm = tahm
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.image = pg.image.load("mons.png") 
        self.image = pg.transform.scale(self.image, (self.width, self.height)) 
        self.rect = self.image.get_rect()  
        self.rect.x = x  # set the x-coordinate of the rect to x
        self.rect.y = y  # set the y-coordinate of the rect to y

    def update(self):
        if self.tahm.rect.x > self.rect.x :
            self.rect.x += 1
        if self.tahm.rect.x < self.rect.x :
            self.rect.x -= 1
        if self.tahm.rect.y > self.rect.y :
            self.rect.y += 1
        if self.tahm.rect.y < self.rect.y :
            self.rect.y -= 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)