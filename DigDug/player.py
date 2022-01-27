import pygame

class Player():
    def __init__(self,settings,screen):
        self.settings = settings #gets a copy of all the settings
        self.screen = screen #gets a copy of the screen
        self.player_color = (200, 30, 80)
        self.xpos = 200
        self.ypos = 200
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        self.direction = "bottom"
        
    def update(self):
        if self.move_right and self.xpos < self.settings.screen_width:
            self.xpos += self.settings.player_speed
            self.direction = "right"
            
        if self.move_left and self.xpos > 300:
            self.xpos -= self.settings.player_speed
            self.direction = "left"
            
        if self.move_up and self.ypos > 200:
            self.ypos -= self.settings.player_speed
            self.direction = "top"
            
        if self.move_down and self.ypos < 800: #this was my mistake; before it was referencing something from the sprite class, which we're not using in my version
            self.ypos += self.settings.player_speed
            self.direction = "bottom"
        
    def draw(self):
        pygame.draw.rect(self.screen, (self.player_color), (self.xpos, self.ypos, 50, 50))