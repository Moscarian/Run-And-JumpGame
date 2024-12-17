import pygame
from sys import exit
from random import randint, choice
from player import Player
from obstacle import Obstacle

width = 800
height = 400

def display_score():
    current_time = pygame.time.get_ticks()//1000 - start_time
    score_surf = test_font.render(f'{current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

# def obstacle_movement(obstacle_list):
#     if obstacle_list:
#         for obstacle_rect in obstacle_list:
#             obstacle_rect.x -= 5
#             if obstacle_rect.bottom == 300:
#                 screen.blit(snail_surface, obstacle_rect)
#             elif obstacle_rect.bottom == 120:
#                 screen.blit(fly_surf, obstacle_rect)
#         obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
#     return obstacle_list

# def player_animation():
#     global player_surf, player_index

#     if player_rect.bottom < 300:
#         player_surf = player_jump
#     else:
#         player_index += 0.1
#         if player_index >= len(player_walk): player_index = 0
#         player_surf = player_walk[int(player_index)]

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("smol pp")
clock = pygame.time.Clock()
test_font = pygame.font.Font('../font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
final_score = 0
background_sound = pygame.mixer.Sound("../audio/music.wav")
background_sound.play(loops = -1)
background_sound.set_volume(0.8)

player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()
obstacle_speed = 10

sky_surface = pygame.image.load("../graphics/Sky.png").convert()
ground_surface = pygame.image.load("../graphics/ground.png").convert()

# score_surface = test_font.render('First game', False, (64,64,64))
# score_rect = score_surface.get_rect(center = (400, 50))

# Obstacle
# snail1 = pygame.image.load("../graphics/snail/snail1.png").convert_alpha()
# snail2 = pygame.image.load("../graphics/snail/snail2.png").convert_alpha()
# snail = [snail1, snail2]
# snail_index = 0
# snail_surface = snail[snail_index]

# fly1 = pygame.image.load("../graphics/Fly/Fly1.png").convert_alpha()
# fly2 = pygame.image.load("../graphics/Fly/Fly2.png").convert_alpha()
# fly = [fly1, fly2]
# fly_index = 0
# fly_surf = fly[fly_index]


# obstacle_rect_list = []

# # Player
# player_walk_1 = pygame.image.load("../graphics/player/player_walk_1.png").convert_alpha()
# player_walk_2 = pygame.image.load("../graphics/player/player_walk_2.png").convert_alpha()
# player_walk = [player_walk_1, player_walk_2]
# player_index = 0
# player_jump = pygame.image.load("../graphics/player/jump.png").convert_alpha()

# player_surf = player_walk[player_index]
# player_rect = player_surf.get_rect(midbottom = (80, 300))
# player_gravity = 0

# Intro screen
player_stand = pygame.image.load("../graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

game_name_surf = test_font.render("Get rid of snails!!",False, (111,196,169))
game_name_rect = game_name_surf.get_rect(center = (400, 80))

instruction_surf = test_font.render("Press space to start",False, (111,196,169))
instruction_rect = instruction_surf.get_rect(center = (400, 350))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 700)

# snail_animation_timer = pygame.USEREVENT + 2
# pygame.time.set_timer(snail_animation_timer, 500)

# fly_animation_timer = pygame.USEREVENT + 3
# pygame.time.set_timer(fly_animation_timer, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
            #         player_gravity = -20
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE and player_rect.bottom == 300:
            #         player_gravity = -20

            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail'])))
                # if randint(0, 2):
                    # obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900,1100), 120)))
                # else:
                #     obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100), 120)))
            # if event.type == snail_animation_timer:
            #     snail_index = 1 - snail_index
            #     snail_surface = snail[snail_index]
            # if event.type == fly_animation_timer:
            #     fly_index = 1 - fly_index
            #     fly_surf = fly[fly_index]
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                obstacle_group.empty()
                start_time = pygame.time.get_ticks()//1000
                obstacle_speed = 10

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        # screen.blit(score_surface, score_rect)
        final_score = display_score()

        # Player
        # player_gravity += 1
        # player_rect.y += player_gravity
        # if player_rect.bottom >= 300:
        #     player_rect.bottom = 300
        # player_animation()
        # screen.blit(player_surf, player_rect)
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
            game_active = False
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # # Collision
        # for obstable_rect in obstacle_rect_list:
        #     if player_rect.colliderect(obstable_rect):
        #         game_active = False

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_name_surf, game_name_rect)

        # (Optional)
        player_gravity = 0
        # player_rect.midbottom = (80, 300)

        score_message = test_font.render(f'Your score: {final_score}',False, (111,196,169))
        score_message_rect = score_message.get_rect(center = (400, 350))
        if final_score == 0:
            screen.blit(instruction_surf, instruction_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)