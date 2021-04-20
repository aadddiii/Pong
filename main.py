import sys
import pygame
import random

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PONG")


def menu():
    game_font_1 = pygame.font.SysFont("calibri", 40, True, True)
    light_grey_1 = (200, 200, 200)



def run_game():
    global player_score, opp_score, ball_speed_y, ball_speed_x

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, oppPlayer)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (400, 0), (400, 600))

    player_text = game_font.render(f"{player_score}", False, light_grey)
    opp_text = game_font.render(f"{opp_score}", False, light_grey)
    screen.blit(player_text, (410, 290))
    screen.blit(opp_text, (380, 290))

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= 600:
        ball_speed_y *= -1

    if ball.left <= 0:
        player_score += 1
        ball.x = 385
        ball.y = 285
        ball_speed_x = -7
        ball_speed_y = 7 * random.choice((-1, 1))

    if ball.right >= 800:
        opp_score += 1
        ball.x = 385
        ball.y = 285
        ball_speed_x = 7
        ball_speed_y = 7 * random.choice((-1, 1))

    if ball.colliderect(player) or ball.colliderect(oppPlayer):
        ball_speed_x *= -1
        ball_speed_y *= 1 * random.choice((-1, 1))

    player.y += player_speed

    if player.top <= 5:
        player.top = 5
    if player.bottom >= 595:
        player.bottom = 595

    if oppPlayer.top <= 5:
        oppPlayer.top = 5
    if oppPlayer.bottom >= 595:
        oppPlayer.bottom = 595

    if oppPlayer.bottom > ball.y:
        oppPlayer.top += -opp_speed
    if oppPlayer.top < ball.y:
        oppPlayer.bottom += opp_speed


ball = pygame.Rect(392, 292, 16, 16)

player = pygame.Rect(790, 250, 5, 100)
player_speed = 0

oppPlayer = pygame.Rect(5, 250, 5, 100)
opp_speed = 7

light_grey = (200, 200, 200)

ball_speed_x = 7 * random.choice((-1, 1))
ball_speed_y = 7 * random.choice((-1, 1))

player_score = 0
opp_score = 0
game_font = pygame.font.SysFont("calibri", 20, True)

runGame = True
while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed += -5
            if event.key == pygame.K_DOWN:
                player_speed += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 5
            if event.key == pygame.K_DOWN:
                player_speed += -5

    run_game()

    pygame.display.flip()
    clock.tick(60)
