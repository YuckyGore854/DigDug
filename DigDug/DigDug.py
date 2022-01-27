import pygame
import os
import game_functions as gf
import digSettings #another python file we're going to write
from player import Player

pygame.init()
game_settings = digSettings.Settings() #creates an object of class Settings
screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
pygame.display.set_caption("DigDug")

player = Player(game_settings, screen) #create player object

while True: #GAME LOOP
    gf.event_listener(screen, game_settings, player)
    player.update()
    gf.update_screen(game_settings, screen, player)
