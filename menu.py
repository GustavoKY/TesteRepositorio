import pygame, sys

# init
pygame.init()

# screen
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

# fonts
font = pygame.font.Font("Perfect DOS VGA 437.ttf", 100)
font_2 = pygame.font.Font("Perfect DOS VGA 437.ttf", 50)

# texts
text = font.render("Teste", True, (255, 255, 255))
play = font_2.render("Play", True, (255, 255, 255))
options = font_2.render("Options", True, (255, 255, 255))
new_game = font_2.render('New Game', True, (255, 255, 255))
load_game = font_2.render('Load Game', True, (255, 255, 255))
X = font_2.render("X", True, (0, 0, 0))
gam = font.render("Game", True, (255, 255, 255))
opt = font.render("Options", True, (255, 255, 255))
save_text = font_2.render('Choose a slot:', True, (255, 255, 255))
slots = (font_2.render('Slot 1', True, (255, 255, 255)), font_2.render('Slot 2', True, (255, 255, 255)),
         font_2.render('Slot 3', True, (255, 255, 255)))


# main menu
def menu():
    menu_select = True
    game_select = False
    load_file = -1
    while True:

        global screen
        screen.fill((0, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if game_select and load_file == -1:
                        game_select = False
                    elif game_select and load_file >= 0:
                        load_file = -1
                    else:
                        pygame.quit()
                        sys.exit()
                if event.key == pygame.K_DOWN:
                    if load_file == -1:
                        menu_select = not menu_select
                    else:
                        if load_file < 2:
                            load_file += 1
                        else:
                            load_file = 0
                if event.key == pygame.K_UP:
                    if load_file == -1:
                        menu_select = not menu_select
                    else:
                        if load_file > 0:
                            load_file -= 1
                        else:
                            load_file = 2
                if event.key == pygame.K_RETURN:
                    if not game_select:
                        if menu_select:
                            game_select = True
                        else:
                            options_m()
                    else:
                        if load_file == -1:
                            if menu_select:
                                game()
                                game_select = False
                            else:
                                load_file = 0
                        else:
                            if load_file == 0:
                                load = open('save00.txt', 'r')
                                game(int(load.readline().rstrip()), int(load.readline().rstrip()),
                                     int(load.readline().rstrip()))
                                load.close()
                            elif load_file == 1:
                                load = open('save01.txt', 'r')
                                game(int(load.readline().rstrip()), int(load.readline().rstrip()),
                                     int(load.readline().rstrip()))
                                load.close()
                            else:
                                load = open('save02.txt', 'r')
                                game(int(load.readline().rstrip()), int(load.readline().rstrip()),
                                     int(load.readline().rstrip()))
                                load.close()


        # buttons
        screen.blit(text, (screen.get_width() / 2 - text.get_rect().width / 2, 100))
        if not game_select:
            screen.blit(play, (screen.get_width() / 2 - play.get_rect().width / 2, 300))
            screen.blit(options, (screen.get_width() / 2 - options.get_rect().width / 2, 380))
        else:
            if load_file == -1:
                screen.blit(new_game, (screen.get_width() / 2 - new_game.get_rect().width / 2, 300))
                screen.blit(load_game, (screen.get_width() / 2 - load_game.get_rect().width / 2, 380))
            else:
                for pos, slt in enumerate(slots):
                    screen.blit(slt, (screen.get_width() / 2 - slt.get_rect().width / 2, 300 + 80 * pos))

        # X mark
        if not game_select:
            if menu_select:
                screen.blit(X, (screen.get_width() / 2 - play.get_rect().width / 2 - X.get_rect().width, 300))
            else:
                screen.blit(X, (screen.get_width() / 2 - options.get_rect().width / 2 - X.get_rect().width, 380))
        else:
            if load_file == -1:
                if menu_select:
                    screen.blit(X, (screen.get_width() / 2 - new_game.get_rect().width / 2 - X.get_rect().width, 300))
                else:
                    screen.blit(X, (screen.get_width() / 2 - load_game.get_rect().width / 2 - X.get_rect().width, 380))
            else:
                screen.blit(X, (screen.get_width() / 2 - slots[0].get_rect().width / 2
                                - X.get_rect().width, 300 + 80 * load_file))

        pygame.display.update()


def game(p_hp=100, p_bllts=50, p_lvl=1):
    player_health_pts = p_hp
    player_bullets = p_bllts
    player_level = p_lvl

    running = True
    while running:

        global screen
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = not running
                if event.key == pygame.K_SPACE:
                    player_health_pts -= 1
                if event.key == pygame.K_s:
                    save_game(player_health_pts, player_bullets, player_level)

        screen.blit(gam, (screen.get_width() / 2 - gam.get_rect().width / 2, 100))
        hp = font_2.render(f'HP:{player_health_pts}', True, (255, 255, 255))
        screen.blit(hp, (0, 0))

        pygame.display.update()


# options
def options_m():
    running = True
    while running:

        global screen
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = not running

        screen.blit(opt, (screen.get_width() / 2 - opt.get_rect().width / 2, 100))

        pygame.display.update()


# save system (Press S to save)
def save_game(hp, bullets, level):
    global screen, slots, X, save_text

    running = True
    slot_select = 0

    # save slots screen
    while running:
        screen.fill((0, 255, 255))
        screen.blit(save_text, (screen.get_width() / 2 - save_text.get_rect().width / 2, 100))
        for pos, slt in enumerate(slots):
            screen.blit(slt, (screen.get_width() / 2 - slt.get_rect().width / 2, 300 + 80 * pos))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if slot_select < 2:
                        slot_select += 1
                    else:
                        slot_select = 0
                if event.key == pygame.K_UP:
                    if slot_select > 0:
                        slot_select -= 1
                    else:
                        slot_select = 2
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_RETURN:
                    if slot_select == 0:
                        save00 = open('save00.txt', 'w')
                        save00.write(str(hp) + '\n')
                        save00.write(str(bullets) + '\n')
                        save00.write(str(level))
                        save00.close()
                    elif slot_select == 1:
                        save01 = open('save01.txt', 'w')
                        save01.write(str(hp) + '\n')
                        save01.write(str(bullets) + '\n')
                        save01.write(str(level))
                        save01.close()
                    else:
                        save02 = open('save02.txt', 'w')
                        save02.write(str(hp) + '\n')
                        save02.write(str(bullets) + '\n')
                        save02.write(str(level))
                        save02.close()
                    running = False
        screen.blit(X, (screen.get_width() / 2 - slots[0].get_rect().width / 2
                        - X.get_rect().width, 300 + 80 * slot_select))
        pygame.display.update()


menu()
