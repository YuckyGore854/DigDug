import pygame

class Settings():
    def __init__(self):
        self.bg_color = (0,0,0)
        
        #get information of the display
        winObject = pygame.display.Info()
        
        #gets height of the screen
        self.screen_height = int(winObject.current_h*.75)
        
        #gets width of the screen
        self.screen_width = int(winObject.current_w*.75)
        
        #Player Settings
        self.player_size = 32
        self.player_speed= .5 #changed this from 2 to .5 to slow player down