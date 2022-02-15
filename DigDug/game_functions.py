import pygame

def listen_press_down(event,screen,settings,player):
    
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        player.move_right = True
        player.move_left = False
        player.move_up = False
        player.move_down = False

    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        player.move_left = True
        player.move_right = False
        player.move_up = False
        player.move_down = False

    if event.key == pygame.K_UP or event.key == pygame.K_w:
        player.move_left = False
        player.move_right = False
        player.move_up = True
        player.move_down = False

    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        player.move_left = False
        player.move_right = False
        player.move_up = False
        player.move_down = True

def listen_press_up(event, player):
    if event.type == pygame.KEYUP:
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.move_right = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.move_left = False
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.move_up = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.move_down = False

def event_listener(screen,settings,player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()#this works on my computer, not sure why it's a bug here
            return 0 #added this to kill game instead

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()

        if event.type == pygame.KEYUP:
            listen_press_up(event,player)

        if event.type == pygame.KEYDOWN:
            listen_press_down(event,screen,settings,player)

def update_screen(settings,screen,player):
    screen.fill(settings.bg_color)
    player.draw()
    pygame.display.flip()